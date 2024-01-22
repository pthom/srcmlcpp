import os

from codemanip import amalgamated_header
import litgen


THIS_DIR = os.path.dirname(__file__)


def make_amalgamated_header() -> None:
    """Generates an amalgamated header file for DaftLib in generated_code/DaftLib_amalgamation/amalgamation.h"""
    options = amalgamated_header.AmalgamationOptions()

    options.base_dir = THIS_DIR + "/cpp_sources"
    options.local_includes_startwith = "DaftLib/"
    options.include_subdirs = ["DaftLib"]
    options.main_header_file = "DaftLib.h"
    options.dst_amalgamated_header_file = THIS_DIR + "/generated_code/DaftLib_amalgamation/amalgamation.h"

    amalgamated_header.write_amalgamate_header_file(options)


def generator_options() -> litgen.LitgenOptions:
    options = litgen.LitgenOptions()

    # The namespace DaftLib will not be emitted as a python submodule: all its contents will be emitted directly in the
    # root of the generated python module
    options.namespaces_root = ["^DaftLib$"]

    # Use BoxedBool for SwitchBool, which can modify its bool parameter
    options.fn_params_replace_modifiable_immutable_by_boxed__regex = "^SwitchBool$"

    return options


def autogenerate_daft_lib(use_amalgamated_header: bool = False) -> None:
    options = generator_options()
    output_cpp_pydef_file = THIS_DIR + "/generated_code/DaftLib_bindings/pybind_DaftLib.cpp"
    output_cpp_glue_code_file = THIS_DIR + "/generated_code/DaftLib_bindings/glue_code_DaftLib.h"
    output_stub_pyi_file = THIS_DIR + "/generated_code/DaftLib_stubs/daft_lib/__init__.pyi"

    # We demonstrate here two methods for generating bindings (both of them work correctly):
    # - either using an amalgamated header
    # - or by providing a list of files to litgen
    if use_amalgamated_header:
        make_amalgamated_header()
        input_cpp_header = THIS_DIR + "/generated_code/DaftLib_amalgamation/amalgamation.h"
        litgen.write_generated_code_for_file(
            options,
            input_cpp_header_file=input_cpp_header,
            output_cpp_pydef_file=output_cpp_pydef_file,
            output_stub_pyi_file=output_stub_pyi_file,
            output_cpp_glue_code_file=output_cpp_glue_code_file,
        )
    else:
        header_files = [
            THIS_DIR + "/cpp_sources/DaftLib/DaftLib.h",
            THIS_DIR + "/cpp_sources/DaftLib/DaftLib_2.h",
        ]
        litgen.write_generated_code_for_files(
            options,
            input_cpp_header_files=header_files,
            output_cpp_pydef_file=output_cpp_pydef_file,
            output_stub_pyi_file=output_stub_pyi_file,
            output_cpp_glue_code_file=output_cpp_glue_code_file,
        )


if __name__ == "__main__":
    autogenerate_daft_lib(use_amalgamated_header=True)
