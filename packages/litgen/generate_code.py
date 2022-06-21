import os
from typing import Callable

from codemanip import code_utils

import srcmlcpp

from litgen.internal import module_pydef_generator, module_stub_generator
from litgen.options import LitgenOptions


def code_to_pydef(options: LitgenOptions, code: str, filename: str = ""):
    from litgen.internal.adapted_types import AdaptedUnit

    cpp_unit = srcmlcpp.code_to_cpp_unit(options.srcml_options, code, filename)
    adapted_unit = AdaptedUnit(cpp_unit, options)
    r = adapted_unit.str_pydef()
    return r


def code_to_stub(options: LitgenOptions, code: str, filename: str = ""):
    from litgen.internal.adapted_types import AdaptedUnit

    cpp_unit = srcmlcpp.code_to_cpp_unit(options.srcml_options, code, filename)
    adapted_unit = AdaptedUnit(cpp_unit, options)
    r = adapted_unit.str_stub()
    return r


def generate_pydef(
    code: str,
    options: LitgenOptions,
    add_boxed_types_definitions: bool = False,
    filename: str = "",
) -> str:

    cpp_unit = srcmlcpp.code_to_cpp_unit(options.srcml_options, code, filename=filename)
    generated_code = module_pydef_generator.generate_pydef(
        cpp_unit, options, add_boxed_types_definitions=add_boxed_types_definitions
    )
    return generated_code


def generate_stub(
    code: str,
    options: LitgenOptions,
    add_boxed_types_definitions: bool = False,
    filename: str = "",
) -> str:
    cpp_unit = srcmlcpp.code_to_cpp_unit(options.srcml_options, code, filename=filename)
    generated_code = module_stub_generator.generate_stub(
        cpp_unit, options, add_boxed_types_definitions=add_boxed_types_definitions
    )

    # Black seems to refuse to see two empty lines at the end of the generated code
    while len(generated_code) > 0 and generated_code[-2:] == "\n\n":
        generated_code = generated_code[:-1]

    return generated_code


def _run_generate_file(
    input_cpp_header: str,
    output_file: str,
    fn_code_generator: Callable,
    marker_token: str,
    options: LitgenOptions,
    add_boxed_types_definitions: bool,
) -> None:
    assert os.path.isfile(input_cpp_header)
    assert os.path.isfile(output_file)

    options.assert_buffer_types_are_ok()

    header_code = code_utils.read_text_file(input_cpp_header)

    generated_code = fn_code_generator(header_code, options, add_boxed_types_definitions, filename=input_cpp_header)

    marker_in = f"<autogen:{marker_token}>"
    marker_out = f"</autogen:{marker_token}>"

    code_utils.write_code_between_markers(output_file, marker_in, marker_out, generated_code)


def generate_files(
    input_cpp_header: str,
    output_cpp_module_file: str,
    options: LitgenOptions,
    output_stub_pyi_file: str = "",
    add_boxed_types_definitions: bool = True,
) -> None:

    _run_generate_file(
        input_cpp_header, output_cpp_module_file, generate_pydef, "pydef_cpp", options, add_boxed_types_definitions
    )

    _run_generate_file(
        input_cpp_header,
        output_stub_pyi_file,
        generate_stub,
        "pyi",
        options,
        add_boxed_types_definitions,
    )
