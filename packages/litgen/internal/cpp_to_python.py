import keyword
from dataclasses import dataclass  # noqa
from typing import List, Optional

from codemanip import code_utils
from codemanip.code_replacements import RegexReplacementList

from srcmlcpp.cpp_types import *
from srcmlcpp.cpp_types.scope.cpp_scope import CppScope, CppScopePart, CppScopeType
from srcmlcpp.cpp_types.template.cpp_i_template_host import CppITemplateHost

from litgen import LitgenOptions
from litgen.internal import LitgenContext


"""
Code utilities for transcription from C++ to Python
"""


def _comment_apply_replacements(options: LitgenOptions, comment: str) -> str:
    """Make some replacements in a C++ comment in order to adapt it to python
    (strip empty lines, remove API markers, apply replacements)
    """
    lines = comment.split("\n")
    if options.python_strip_empty_comment_lines:
        lines = code_utils.strip_empty_lines_in_list(lines)
    if len(lines) == 0:
        return ""

    if len(lines) == 0:
        return ""

    lines = code_utils.strip_lines_right_space(lines)

    comment = "\n".join(lines)
    comment = options.comments_replacements.apply(comment)

    return comment


def comment_pydef_one_line(options: LitgenOptions, title_cpp: str) -> str:
    """Formats a docstring on one cpp line. Used only in cpp pydef bindings code"""
    r = code_utils.format_cpp_comment_on_one_line(_comment_apply_replacements(options, title_cpp))
    r = _comment_apply_replacements(options, r)
    return r


def type_to_python(options: LitgenOptions, type_cpp: str) -> str:
    r = type_cpp
    r = r.replace("static ", "")
    r = options.type_replacements.apply(r).strip()
    return r


def add_underscore_if_python_reserved_word(name: str) -> str:
    if name in keyword.kwlist:
        name += "_"
    return name


def _class_name_to_python(options: LitgenOptions, name: str) -> str:  # noqa
    name_with_replacements = options.type_replacements.apply(name)
    name_with_replacements = add_underscore_if_python_reserved_word(name_with_replacements)
    return name_with_replacements


def enum_name_to_python(options: LitgenOptions, name: str) -> str:  # noqa
    name_with_replacements = options.type_replacements.apply(name)
    name_with_replacements = add_underscore_if_python_reserved_word(name_with_replacements)
    return name_with_replacements


def function_name_to_python(options: LitgenOptions, name: str) -> str:
    name_with_replacements = options.function_names_replacements.apply(name)
    if options.python_convert_to_snake_case:
        name_snake_case = code_utils.to_snake_case(name_with_replacements)
        r = add_underscore_if_python_reserved_word(name_snake_case)
    else:
        r = add_underscore_if_python_reserved_word(name_with_replacements)
    r = options.function_names_replacements.apply(r)
    return r


def namespace_name_to_python(options: LitgenOptions, name: str) -> str:
    name_with_replacements = options.namespace_names_replacements.apply(name)
    if options.python_convert_to_snake_case:
        name_snake_case = code_utils.to_snake_case(name_with_replacements)
        r = add_underscore_if_python_reserved_word(name_snake_case)
    else:
        r = add_underscore_if_python_reserved_word(name_with_replacements)
    r = options.var_names_replacements.apply(r)
    return r


def var_name_to_python(options: LitgenOptions, name: str) -> str:
    name_with_replacements = options.var_names_replacements.apply(name)
    if options.python_convert_to_snake_case:
        name_snake_case = code_utils.to_snake_case(name_with_replacements)
        r = add_underscore_if_python_reserved_word(name_snake_case)
    else:
        r = add_underscore_if_python_reserved_word(name_with_replacements)
    r = options.var_names_replacements.apply(r)
    return r


def var_value_to_python(context: LitgenContext, default_value_cpp: str) -> str:
    r = default_value_cpp
    r = context.options.type_replacements.apply(r)
    r = context.options.value_replacements.apply(r)
    for number_macro, value in context.options.srcmlcpp_options.named_number_macros.items():
        r = r.replace(number_macro, str(value))
    r = context.var_values_replacements_cache.apply(r)
    return r


def is_float_str(s: str) -> bool:
    try:
        _ = float(s)
    except ValueError:
        return False
    return True


def cpp_type_to_camel_case_no_space(cpp_type: str) -> str:
    items = cpp_type.split(" ")

    def capitalize_first_letter(s: str) -> str:
        return s[0].upper() + s[1:]

    items = list(map(capitalize_first_letter, items))

    r = "".join(items)
    return r


@dataclass
class CppPythonTypesSynonyms:
    cpp_type: str
    python_type: str


CPP_PYTHON_NUMERIC_INT_SYNONYMS = [
    CppPythonTypesSynonyms("int", "int"),
    CppPythonTypesSynonyms("unsigned int", "int"),
    CppPythonTypesSynonyms("signed int", "int"),
    CppPythonTypesSynonyms("long", "int"),
    CppPythonTypesSynonyms("unsigned long", "int"),
    CppPythonTypesSynonyms("signed long", "int"),
    CppPythonTypesSynonyms("long long", "int"),
    CppPythonTypesSynonyms("unsigned long long", "int"),
    CppPythonTypesSynonyms("signed long long", "int"),
    CppPythonTypesSynonyms("uint8_t", "int"),
    CppPythonTypesSynonyms("int8_t", "int"),
    CppPythonTypesSynonyms("uint16_t", "int"),
    CppPythonTypesSynonyms("int16_t", "int"),
    CppPythonTypesSynonyms("uint32_t", "int"),
    CppPythonTypesSynonyms("int32_t", "int"),
    CppPythonTypesSynonyms("uint64_t", "int"),
    CppPythonTypesSynonyms("int64_t", "int"),
    CppPythonTypesSynonyms("size_t", "int"),
    CppPythonTypesSynonyms("ssize_t", "int"),
    CppPythonTypesSynonyms("std::size_t", "int"),
]

CPP_PYTHON_NUMERIC_FLOAT_SYNONYMS = [
    CppPythonTypesSynonyms("float", "float"),
    CppPythonTypesSynonyms("double", "float"),
    CppPythonTypesSynonyms("long double", "float"),
]


CPP_PYTHON_NUMERIC_SYNONYMS = CPP_PYTHON_NUMERIC_INT_SYNONYMS + CPP_PYTHON_NUMERIC_FLOAT_SYNONYMS


def cpp_numeric_types() -> List[str]:
    r = []
    for t in CPP_PYTHON_NUMERIC_SYNONYMS:
        r.append(t.cpp_type)
    return r


def is_cpp_type_immutable_for_python(cpp_type: str) -> bool:
    if cpp_type in cpp_numeric_types():
        return True
    if cpp_type in ["string", "std::string", "bool"]:
        return True
    # Etc: handle tuple and complex numbers?
    return False


"""
In python and numpy we have the following correspondence:

Given a py::array, we can get its inner type with a char identifier like this:
    char array_type = array.dtype().char_();

Here is the table of correspondences:
"""
_PY_ARRAY_TYPE_TO_CPP_TYPE = {
    "B": "uint8_t",
    "b": "int8_t",
    "H": "uint16_t",
    "h": "int16_t",
    "I": "uint32_t",
    "i": "int32_t",
    "L": "np_uint_l",  # Platform dependent: "uint64_t" on *nixes, "uint32_t" on windows
    "l": "np_int_l",  # Platform dependent: "int64_t" on *nixes, "int32_t" on windows
    "f": "float",
    "d": "double",
    "g": "long double",
    "q": "long long",
}


def py_array_types() -> List[str]:
    r: List[str] = []
    for type_ in _PY_ARRAY_TYPE_TO_CPP_TYPE.keys():
        r.append(type_)
    return r


def py_array_type_to_cpp_type(py_array_type: str) -> str:
    assert len(py_array_type) == 1
    assert py_array_type in _PY_ARRAY_TYPE_TO_CPP_TYPE
    return _PY_ARRAY_TYPE_TO_CPP_TYPE[py_array_type]


def cpp_type_to_py_array_type(cpp_type: str) -> str:
    cpp_type = cpp_type.strip()
    if cpp_type.endswith("*"):
        cpp_type = cpp_type[:-1].strip()
    if cpp_type.startswith("const "):
        cpp_type = cpp_type.replace("const ", "").strip()
    for py_type, tested_cpp_type in _PY_ARRAY_TYPE_TO_CPP_TYPE.items():
        if tested_cpp_type == cpp_type:
            return py_type
    raise ValueError(f"cpp_type_to_py_array_type: unhandled type {cpp_type}")


##################################################################################################################
#
# CppElements related below (migrate to adapted_types sub package later ?)
#
##################################################################################################################


def decl_python_var_name(options: LitgenOptions, cpp_decl: CppDecl) -> str:
    var_cpp_name = cpp_decl.decl_name
    var_python_name = var_name_to_python(options, var_cpp_name)
    return var_python_name


def decl_python_value(context: LitgenContext, cpp_decl: CppDecl) -> str:
    value_cpp = cpp_decl.initial_value_code
    value_python = var_value_to_python(context, value_cpp)
    return value_python


def info_original_location(options: LitgenOptions, cpp_element: CppElement, comment_token: str) -> str:
    if not options.original_location_flag_show:
        return ""

    nb_folders = options.original_location_nb_parent_folders
    header_file = cpp_element.filename
    if header_file is not None:
        header_file = code_utils.filename_with_n_parent_folders(header_file, nb_folders)
    else:
        header_file = "Line"

    _i_ = options.indent_cpp_spaces()

    start = cpp_element.start()
    line = start.line if start is not None else "unknown line"
    r = f"{_i_}{comment_token} {header_file}:{line}"
    return r


def info_original_location_cpp(options: LitgenOptions, cpp_element: CppElement) -> str:
    return info_original_location(options, cpp_element, "//")


def info_original_location_python(options: LitgenOptions, cpp_element: CppElement) -> str:
    return info_original_location(options, cpp_element, "#")


def docstring_lines(options: LitgenOptions, cpp_element_c: CppElementAndComment) -> List[str]:
    """Return the comment of a CppElement under the form of a docstring, such as the one you are reading.
    Some replacements will be applied (for example true -> True, etc)
    """

    docstring = cpp_element_c.cpp_element_comments.full_comment()
    docstring = _comment_apply_replacements(options, docstring)
    if docstring.startswith('"'):
        docstring = " " + docstring
    if docstring.endswith('"'):
        docstring = docstring + " "

    if len(docstring) == 0:
        return []

    lines = docstring.split("\n")

    r = []  # noqa
    r.append('''"""''' + lines[0])
    r += lines[1:]

    if len(r) == 1:
        r[0] += '''"""'''
    else:
        r.append('"""')

    return r


def comment_python_shall_place_at_end_of_line(options: LitgenOptions, cpp_element_c: CppElementAndComment) -> bool:
    if not options.python_reproduce_cpp_layout:
        return False
    eol_comment = _comment_apply_replacements(options, cpp_element_c.cpp_element_comments.comment_end_of_line)
    previous_lines_comment = _comment_apply_replacements(
        options, cpp_element_c.cpp_element_comments.comment_on_previous_lines
    )
    return len(eol_comment) > 0 and len(previous_lines_comment) == 0


def comment_python_end_of_line(options: LitgenOptions, cpp_element_c: CppElementAndComment) -> str:
    eol_comment = _comment_apply_replacements(options, cpp_element_c.cpp_element_comments.comment_end_of_line)
    if len(eol_comment) > 0:
        eol_comment_with_token = "  #" + eol_comment
        return eol_comment_with_token
    else:
        return ""


def comment_python_previous_lines(options: LitgenOptions, cpp_element_c: CppElementAndComment) -> List[str]:
    """See comment below"""
    # Returns the comment of a CppElement under the form of a python comment, such as the one you are reading.
    # Some replacements will be applied (for example true -> True, etc)

    comment = cpp_element_c.cpp_element_comments.full_comment()
    if isinstance(cpp_element_c, CppComment):
        comment = cpp_element_c.comment

    comment = _comment_apply_replacements(options, comment)

    if len(comment) == 0:
        return []

    lines = comment.split("\n")

    def add_sharp(s: str) -> str:
        if options.python_reproduce_cpp_layout:
            return "#" + s
        else:
            return "# " + s.lstrip()

    lines = list(map(add_sharp, lines))
    lines = code_utils.strip_lines_right_space(lines)

    return lines


def enum_element_is_count(options: LitgenOptions, enum: CppEnum, enum_element: CppDecl) -> bool:
    if not options.enum_flag_skip_count:
        return False

    is_class_enum = enum.enum_type == "class"
    value_name = enum_element.decl_name

    if not code_utils.does_match_regex(options.fn_params_buffer_size_names__regex, value_name):
        return False

    if is_class_enum:
        return True
    else:
        has_enum_name_part = code_utils.var_name_contains_word(value_name.lower(), enum.enum_name.lower())
        return has_enum_name_part


def looks_like_size_param(options: LitgenOptions, param_c: CppParameter) -> bool:
    r = code_utils.does_match_regex(options.fn_params_buffer_size_names__regex, param_c.decl.decl_name)
    return r


def apply_black_formatter_pyi(options: LitgenOptions, code: str) -> str:
    if not options.python_run_black_formatter:
        return code

    import black

    black_mode = black.Mode()
    black_mode.is_pyi = True
    black_mode.target_versions = {black.TargetVersion.PY39}
    black_mode.line_length = options.python_black_formatter_line_length

    formatted_code = black.format_str(code, mode=black_mode)
    return formatted_code


def _scope_part_name(scope_part: CppScopePart) -> str:
    r = ""
    if scope_part.scope_type == CppScopeType.ClassOrStruct:
        r += "Class"
    elif scope_part.scope_type == CppScopeType.Namespace:
        r += "Ns"
    elif scope_part.scope_type == CppScopeType.Namespace:
        r += "Enum"
    r += scope_part.scope_name
    return r


def cpp_scope_to_pybind_scope(options: LitgenOptions, cpp_element: CppElement, include_self: bool) -> CppScope:
    """Remove namespaces considered as root namespace in the options
    (it requires to add a using namespace in the pybind_xxx.cpp file, but this is ok)
    """
    cpp_scope = cpp_element.cpp_scope(include_self)
    scope_parts = cpp_scope.scope_parts

    scope_parts_excluding_namespaces: List[CppScopePart] = []
    for scope_part in scope_parts:
        if scope_part.scope_type != CppScopeType.Namespace:
            scope_parts_excluding_namespaces.append(scope_part)
        else:
            is_root = code_utils.does_match_regex(options.namespace_root__regex, scope_part.scope_name)
            if not is_root:
                scope_parts_excluding_namespaces.append(scope_part)

    cpp_scope.scope_parts = scope_parts_excluding_namespaces
    return cpp_scope


def cpp_scope_to_pybind_scope_str(options: LitgenOptions, cpp_element: CppElement, include_self: bool) -> str:
    scope = cpp_scope_to_pybind_scope(options, cpp_element, include_self)
    scope_names = [scope_part.scope_name for scope_part in scope.scope_parts]
    r = ".".join(scope_names)
    return r


def cpp_scope_to_pybind_var_name(options: LitgenOptions, cpp_element: CppElement) -> str:
    cpp_scope = cpp_scope_to_pybind_scope(options, cpp_element, True)
    scope_parts_strs = list(map(_scope_part_name, cpp_scope.scope_parts))
    if len(scope_parts_strs) > 0:
        r = "py" + "_".join(scope_parts_strs)
        if isinstance(cpp_element, CppITemplateHost):
            if len(cpp_element.specialized_template_params) > 0:
                instantiated_template_params_str = [str(param) for param in cpp_element.specialized_template_params]
                instantiated_template_params_str = [
                    param.replace(" ", "_").replace("std::", "").replace("::", "_")
                    for param in instantiated_template_params_str
                ]
                r += "_" + "_".join(instantiated_template_params_str)
    else:
        r = "m"
    return r


def cpp_scope_to_pybind_parent_var_name(options: LitgenOptions, cpp_element: CppElement) -> str:
    cpp_scope = cpp_scope_to_pybind_scope(options, cpp_element, False)
    if len(cpp_scope.scope_parts) == 0:
        return "m"
    else:
        scope_parts_strs = map(_scope_part_name, cpp_scope.scope_parts)
        r = "py" + "_".join(scope_parts_strs)
        return r


def standard_type_replacements() -> RegexReplacementList:
    """Replacements for C++ code when translating to python.

    Consists mostly of
    * types translations
    * NULL, nullptr, void translation
    * number translation (e.g. `1.5f` -> `1.5`)
    """
    replacements_str = r"""
    \bunsigned \s*int\b -> int
    \bunsigned \s*short\b -> int
    \bunsigned \s*long long\b -> int
    \bunsigned \s*long\b -> int
    \buint8_t\b -> int
    \bint8_t\b -> int
    \buint16_t\b -> int
    \bint16_t\b -> int
    \buint32_t\b -> int
    \bint32_t\b -> int
    \buint64_t\b -> int
    \bint64_t\b -> int
    \blong\b -> int
    \bshort\b -> int
    \\blong \s*long\b -> int
    \blong \s*long\b -> int

    \blong \s*double\b -> float
    \bdouble\b -> float
    \bfloat\b -> float

    \bconst \s*char*\b -> str
    \bconst \s*char *\b -> str

    \bsize_t\b -> int
    \bstd::string\(\) -> ""
    \bstd::string\b -> str
    \bstd::vector\s*<\s*([\w:]*)\s*> -> List[\1]
    \bstd::array\s*<\s*([\w:]*)\s*,\s*([\w:]*)\s*> -> List[\1]
    \bstd::tuple<(.*)> -> Tuple[\1]
    \bstd::optional<(.*?)> -> Optional[\1]
    \bstd::unique_ptr<(.*?)> -> \1
    \bstd::shared_ptr<(.*?)> -> \1
    \bstd::map<\s*([\w:]*)\s*,\s*([\w:]*)\s*> -> Dict[\1, \2]

    \bvoid\s*\* -> Any
    \bvoid\b -> None

    \bpy::array\b -> np.ndarray

    \bconst\b -> REMOVE
    \bmutable\b -> REMOVE
    & -> REMOVE
    \* -> REMOVE

    :: -> .
    """
    # Note: the two last regexes replace C numbers like 1.5f or 1.5d by 1.5

    replaces = RegexReplacementList.from_string(replacements_str)
    return replaces


def standard_value_replacements() -> RegexReplacementList:
    """Replacements for C++ code when translating to python.

    Consists mostly of
    * number translation (e.g. `1.5f` -> `1.5`)
    """
    replacements_str = r"""

    \btrue\b -> True
    \bfalse\b -> False
    \bvoid\s*\* -> Any
    \bvoid\b -> None
    \bNULL\b -> None
    \bnullptr\b -> None
    \std::nullopt\b -> None
    ^std::nullopt\b$ -> None
    \std.nullopt\b -> None
    ^std.nullopt\b$ -> None

    \bstd::string\(\) -> ""
    \bstd.string\(\) -> ""

    \bFLT_MIN\b -> sys.float_info.min
    \bFLT_MAX\b -> sys.float_info.max
    \bDBL_MIN\b -> sys.float_info.min
    \bDBL_MAX\b -> sys.float_info.max
    \bLDBL_MIN\b -> sys.float_info.min
    \bLDBL_MAX\b -> sys.float_info.max


    ([+-]?[0-9]+([.][0-9]*)?|[.][0-9]+)(d?) -> \1
    ([+-]?[0-9]+([.][0-9]*)?|[.][0-9]+)(f?) -> \1

    :: -> .
    """
    # Note: the two last regexes replace C numbers like 1.5f or 1.5d by 1.5

    replaces = RegexReplacementList.from_string(replacements_str)
    return replaces


def standard_comment_replacements() -> RegexReplacementList:
    """Replacements for C++ code when translating to python.

    Consists mostly of
    * bool translation
    * NULL, nullptr, void translation
    * number translation (e.g. `1.5f` -> `1.5`)
    """
    replacements_str = r"""

    \btrue\b -> True
    \bfalse\b -> False

    \bvoid\b -> None
    \bNULL\b -> None
    \bnullptr\b -> None

    ([+-]?[0-9]+([.][0-9]*)?|[.][0-9]+)(d?) -> \1
    ([+-]?[0-9]+([.][0-9]*)?|[.][0-9]+)(f?) -> \1
    """

    # Note: the two last regexes replace C numbers like 1.5f or 1.5d by 1.5
    return RegexReplacementList.from_string(replacements_str)


def opencv_replacements() -> RegexReplacementList:
    replacements_str = r"""
    \bcv::Size\(\) -> (0, 0)
    \bcv::Point\(-1, -1\) -> (-1, -1)
    \bcv::Point2d\(-1., -1.\) -> (-1., -1.)
    \bcv::Size\b -> Size
    \bcv::Matx33d::eye\(\) -> np.eye(3)
    \bcv::Matx33d\b -> Matx33d
    \bcv::Mat\b -> np.ndarray
    \bcv::Point\b -> Point
    \bcv::Point2d\b -> Point2d
    """
    return RegexReplacementList.from_string(replacements_str)


def cpp_type_default_python_value(cpp_type: str) -> Optional[str]:
    for synonym in CPP_PYTHON_NUMERIC_INT_SYNONYMS:
        if synonym.cpp_type == cpp_type:
            return "0"
    for synonym in CPP_PYTHON_NUMERIC_FLOAT_SYNONYMS:
        if synonym.cpp_type == cpp_type:
            return "0."
    if cpp_type in ["std::string", "string"]:
        return '""'
    if cpp_type in ["bool"]:
        return "false"

    return None


def _surround_code_with_filename_impl(
    options: LitgenOptions, filename: Optional[str], code: str, decoration_token: str
) -> str:
    if filename is None or len(filename) == 0:
        return code

    filename_short = code_utils.filename_with_n_parent_folders(filename, options.original_location_nb_parent_folders)

    def decorate_impl(is_end: bool) -> str:
        end_marker = "/" if is_end else ""
        decoration = decoration_token * 20
        r = f"{decoration}    <{end_marker}generated_from:{filename_short}>    {decoration}\n"
        return r

    intro = decorate_impl(False)
    outro = decorate_impl(True)
    r = intro + code + outro
    return r


def surround_cpp_code_with_filename(options: LitgenOptions, filename: Optional[str], code: str) -> str:
    return _surround_code_with_filename_impl(options, filename, code, "/")


def surround_python_code_with_filename(options: LitgenOptions, filename: Optional[str], code: str) -> str:
    return _surround_code_with_filename_impl(options, filename, code, "#")


def surround_python_code_lines(code_lines: List[str], message: str) -> List[str]:
    intro = code_utils.unindent_code(
        f"""
    #  ------------------------------------------------------------------------
    #      <{message}>
    """,
        flag_strip_empty_lines=True,
    ).split("\n")

    outro = code_utils.unindent_code(
        f"""
    #      </{message}>
    #  ------------------------------------------------------------------------
    """,
        flag_strip_empty_lines=True,
    ).split("\n")

    r = intro + code_lines + outro
    return r
