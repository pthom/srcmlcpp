#!/usr/bin/env python3
from dataclasses import dataclass
import os
from sys import version_info
from typing import List


@dataclass
class AmalgamationOptions:
    base_dir: str
    local_includes_startwith: str
    include_subdirs: List[str]

    main_header_file: str
    dst_amalgamated_header_file: str

    def __init__(self) -> None:
        self.base_dir = ""
        self.local_includes_startwith = ""
        self.include_subdirs = []
        self.main_header_file = ""
        self.dst_amalgamated_header_file = ""


AUTOGENERATED_HEADER = "// THIS FILE WAS GENERATED AUTOMATICALLY. DO NOT EDIT.\n"


def _fread_lines(filename: str) -> List[str]:
    """
    Python 2 & 3 agnostic fopen + readlines
    """
    if version_info[0] >= 3:
        f = open(filename, "r", encoding="utf-8", errors="ignore")
    else:
        f = open(filename, "r")
    return f.readlines()


def _fread_content(filename: str) -> str:
    """
    Python 2 & 3 agnostic fopen + readlines
    """
    if version_info[0] >= 3:
        f = open(filename, "r", encoding="utf-8", errors="ignore")
    else:
        f = open(filename, "r")
    return f.read()


def _fwrite_content(filename: str, content: str) -> None:
    """
    Python 2 & 3 agnostic fopen + write
    This function will not overwrite the file (and thus not update its modification date)
    if the new content is unchanged
    """
    if os.path.isfile(filename):
        old_content = _fread_content(filename)
        if old_content == content:
            return

    if version_info[0] >= 3:
        f = open(filename, "w", encoding="utf-8", errors="ignore")
    else:
        f = open(filename, "w")
    f.write(content)
    f.close()


def _is_local_include_line(options: AmalgamationOptions, code_line: str) -> bool:
    """
    Tests whether a C++ code line is a local include statement
    (i.e this will *exclude* lines like "#include <vector>")
    """
    result = False
    if code_line.startswith(f"#include <{options.local_includes_startwith}"):
        result = True
    if code_line.startswith(f'#include "{options.local_includes_startwith}'):
        result = True
    return result


def _is_external_include_line(options: AmalgamationOptions, code_line: str) -> bool:
    if not code_line.startswith("#include "):
        return False
    if _is_local_include_line(options, code_line):
        return False
    return True


def _extract_local_include_file(code_line: str) -> str:
    """
    Extracts the included file path from an include statement
    """
    result = code_line.replace('#include "', "").replace('"', "").replace(">", "")[:-1]
    # possible_include_paths = [ 'immvision/', 'immdebug/']
    # for possible_include_path in possible_include_paths:
    #     result = result.replace(possible_include_path, "")
    return result


def _extract_external_include_file(code_line: str) -> str:
    result: str = code_line.replace("#include ", "").replace("\n", "")
    if "#" in result:
        result = result[: result.index("#")]
    return result


def _decorate_code_info(info: str) -> str:
    separator_line = "//////////////////////////////////////////////////////////////////////////////////////////////////////////////////"
    middle_line = f"//                       {info}".ljust(len(separator_line) - 2) + "//"
    result = f"""
{separator_line}
{middle_line}
{separator_line}
"""
    return result


def _amalgamate_one_file(
    options: AmalgamationOptions,
    included_filename: str,
    including_filename: str,
    already_included_local_files: List[str],
    already_included_external_files: List[str],
) -> str:
    """
    Recursive function that will create an amalgamation for a given header file.
    """
    included_filename_full_path = f"{options.base_dir}/{included_filename}"
    if not os.path.isfile(included_filename_full_path):
        for include_subdir in options.include_subdirs:
            proposed_path = f"{options.base_dir}/{include_subdir}/{included_filename}"
            if os.path.isfile(proposed_path):
                included_filename_full_path = proposed_path

    if not os.path.isfile(included_filename_full_path):
        raise FileNotFoundError(included_filename)

    if included_filename_full_path in already_included_local_files:
        return ""

    already_included_local_files.append(included_filename_full_path)

    included_filename_relative = included_filename.replace(options.base_dir + "/", "").replace(options.base_dir, "")

    if len(including_filename) > 0:
        header = _decorate_code_info(f"{included_filename_relative} included by {including_filename}")
    else:
        header = _decorate_code_info(included_filename_relative)
    parsed_result = header

    lines = _fread_lines(included_filename_full_path)
    was_file_interrupted_by_include = False
    for code_line in lines:
        if (
            was_file_interrupted_by_include
            and len(code_line.strip()) > 0
            and not _is_local_include_line(options, code_line)
        ):
            parsed_result = parsed_result + _decorate_code_info(included_filename_relative + " continued") + "\n"
            was_file_interrupted_by_include = False
        if _is_external_include_line(options, code_line):
            external_file = _extract_external_include_file(code_line)
            if external_file not in already_included_external_files:
                parsed_result = parsed_result + code_line
                already_included_external_files.append(external_file)
        elif _is_local_include_line(options, code_line):
            new_file = _extract_local_include_file(code_line)
            include_addition = _amalgamate_one_file(
                options,
                new_file,
                included_filename_relative,
                already_included_local_files,
                already_included_external_files,
            )
            if len(include_addition) > 0:
                parsed_result = parsed_result + include_addition
                was_file_interrupted_by_include = True
        else:
            if "#pragma once" not in code_line:
                parsed_result = parsed_result + code_line

    is_code_composed_of_only_blank_lines = True
    for line in parsed_result.split("\n"):
        if len(line.strip()) != 0:
            is_code_composed_of_only_blank_lines = False
    if is_code_composed_of_only_blank_lines:
        return ""

    return parsed_result


def _find_all_files_of_extension(folder: str, extension: str) -> List[str]:
    found_files = []
    for root, _dirs, files in os.walk(folder, topdown=False):
        for name in files:
            if name.endswith(extension):
                found_file = root + "/" + name
                found_file = found_file.replace("\\", "/")
                found_file = found_file.replace(folder + "/", "")
                found_files.append(found_file)
    return found_files


def _trim_trailing_spaces(content: str) -> str:
    lines = content.split("\n")
    lines = list(map(lambda s: s.rstrip(), lines))
    trimmed = "\n".join(lines)
    return trimmed


def write_amalgamate_header_file(options: AmalgamationOptions) -> None:
    content = _amalgamate_one_file(options, options.main_header_file, "", [], [])
    content = AUTOGENERATED_HEADER + content
    content = _trim_trailing_spaces(content)
    _fwrite_content(options.dst_amalgamated_header_file, content)
