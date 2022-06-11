import os, sys; _THIS_DIR = os.path.dirname(__file__); sys.path.append(_THIS_DIR + "/../..")

import srcmlcpp
from srcmlcpp import srcml_main
from litgen.internal import code_utils, module_pydef_generator
import litgen


def read_file_content(filename):
    with open(filename, "r") as f:
        content = f.read()
    return content


def play_parse(code):
    options = litgen.code_style_imgui()
    cpp_unit = srcmlcpp.code_to_cpp_unit(options, code)
    print(cpp_unit)




def play_imgui():
    options = litgen.code_style_imgui()
    source_filename = os.path.realpath(_THIS_DIR + "/../../examples_real_libs/imgui/imgui/imgui.h")
    cpp_unit = srcmlcpp.file_to_cpp_unit(options.srcml_options, source_filename)
    # print(cpp_unit)

def play_implot():
    options = litgen.code_style_implot()
    options.flag_show_original_location_in_pybind_file = True
    source_filename = os.path.realpath(_THIS_DIR + "/../../examples_real_libs/implot/implot/implot.h")
    cpp_unit = srcmlcpp.file_to_cpp_unit(options.srcml_options, source_filename)
    # print(cpp_unit)
    pydef_code = module_pydef_generator.generate_pydef(cpp_unit, options)
    print(pydef_code)


def play_pydef(code):
    # options = litgen.options.code_style_implot()
    # options.srcml_options.functions_api_prefixes = ["MY_API"]
    # options.srcml_options.api_suffixes = ["MY_API"]

    # options = litgen.options.CodeStyleOptions()
    # options.indent_cpp_size = 4
    # options.indent_cpp_with_tabs = False

    options = litgen.code_style_imgui()

    options.flag_show_original_location_in_pybind_file = True

    # from srcmlcpp import srcml_utils
    # xml = srcmlcpp.code_to_srcml(code)
    # print(srcml_utils.srcml_to_str_readable(xml))

    pydef_code = litgen.generate_pydef(code, options, add_boxed_types_definitions=True)
    print(f">>>\n{pydef_code}<<<")

#test_code()


# IMGUI_API bool          Combo(const char* label, int* current_item, const char* const items[], int items_count);
# options = code_style_implot()
# options.srcml_options.functions_api_prefixes = ["MY_API"]
# play_parse(code)
code = """
    IMGUI_API inline void change_c_array2(unsigned long values[2]);
"""
play_pydef(code)
# play_imgui()

# play_implot()


# import litgen
# options = litgen.CodeStyleOptions()
# options.srcml_options.functions_api_prefixes = ["MY_API", "IMGUI_API"]
# code = """
# const char ** const items=some_default_value();
# """
#
# pydef_code = litgen.generate_pydef(code, options)
# print(pydef_code)