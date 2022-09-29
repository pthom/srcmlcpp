# type: ignore
import sys
from typing import Literal, List, Any, Optional, Tuple
import numpy as np
from enum import Enum
import numpy

# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!  AUTOGENERATED CODE !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# <litgen_stub> // Autogenerated code below! Do not edit!
####################    <generated_from:BoxedTypes>    ####################
class BoxedInt:
    value: int
    def __init__(self, v: int = 0) -> None:
        pass
    def __repr__(self) -> str:
        pass
class BoxedBool:
    value: bool
    def __init__(self, v: bool = False) -> None:
        pass
    def __repr__(self) -> str:
        pass
class BoxedUnsignedLong:
    value: int
    def __init__(self, v: int = 0) -> None:
        pass
    def __repr__(self) -> str:
        pass
class BoxedString:
    value: str
    def __init__(self, v: str = "") -> None:
        pass
    def __repr__(self) -> str:
        pass
####################    </generated_from:BoxedTypes>    ####################


####################    <generated_from:mylib_amalgamation.h>    ####################
# THIS FILE WAS GENERATED AUTOMATICALLY. DO NOT EDIT.

#////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#                       mylib/mylib.h                                                                          //
#//////////////////////////////////////////////////////////////////////////////////////////////////////////////

#////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#                       mylib/api_marker.h included by mylib/mylib.h                                           //
#//////////////////////////////////////////////////////////////////////////////////////////////////////////////


#////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#                       mylib/basic_test.h included by mylib/mylib.h                                           //
#//////////////////////////////////////////////////////////////////////////////////////////////////////////////

def my_sub(a: int, b: int) -> int:
    """ Subtracts two numbers: this will be the function's __doc__ since my_sub does not have an end-of-line comment"""
    pass


# Title that should be published as a top comment in python stub (pyi) and thus not part of __doc__
# (the end-of-line comment will supersede this top comment)
def my_add(a: int, b: int) -> int:
    """ Adds two numbers"""
    pass


# my_mul should have no user doc (but it will have a typing doc generated by pybind)
# (do not remove the next empty line, or this comment would become my_mul's doc!)

def my_mul(a: int, b: int) -> int:
    pass



#For info, below is the python pyi stub that is published for this file:
#
#def my_sub(a: int, b: int) -> int:
#    """ Subtracts two numbers: this will be the __doc__ since my_sub does not have an end-of-line comment"""
#    pass
#
#
## Title that should be published as a top comment in python stub (pyi) and thus not part of __doc__
## (the end-of-line comment will supersede the top comment)
#def my_add(a: int, b: int) -> int:
#    """ Adds two numbers"""
#    pass
#
#
## my_mul should have no user doc (but it will have a typing doc generated by pybind)
## (do not remove the next empty line, or this comment would become my_mul's doc!)
#
#def my_mul(a: int, b: int) -> int:
#    pass

#////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#                       mylib/header_filter_test.h included by mylib/mylib.h                                   //
#//////////////////////////////////////////////////////////////////////////////////////////////////////////////

# Here, we test that functions placed under unknown preprocessor conditions are not exported by default
# You could choose to add them anyway with:
#    options.srcml_options.header_filter_acceptable_suffixes += "|OBSCURE_OPTION"


#////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#                       mylib/c_style_array_test.h included by mylib/mylib.h                                   //
#//////////////////////////////////////////////////////////////////////////////////////////////////////////////

# C Style array tests


def const_array2_add(values: List[int]) -> int:
    """ Tests with const array: since the input numbers are const, their params are published as List[int],
     and the python signature will be:
     -->    def add_c_array2(values: List[int]) -> int:
     (and the runtime will check that the list size is exactly 2)
    """
    pass


def array2_modify(
    values_0: BoxedUnsignedLong,
    values_1: BoxedUnsignedLong
    ) -> None:
    """ Test with a modifiable array: since the input array is not const, it could be modified.
     Thus, it will be published as a function accepting Boxed values:
     -->    def array2_modify(values_0: BoxedUnsignedLong, values_1: BoxedUnsignedLong) -> None:
    """
    pass

class Point2:
    x: int
    y: int

def array2_modify_mutable(out_0: Point2, out_1: Point2) -> None:
    """ Test with a modifiable array that uses a user defined struct.
     Since the user defined struct is mutable in python, it will not be Boxed,
     and the python signature will be:
    -->    def get_points(out_0: Point2, out_1: Point2) -> None:
    """
    pass

#////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#                       mylib/c_style_buffer_to_pyarray_test.h included by mylib/mylib.h                       //
#//////////////////////////////////////////////////////////////////////////////////////////////////////////////


# C Style buffer to py::array tests
#
# litgen is able to recognize and transform pairs of params whose C++ signature resemble
#     (T* data, size_t|int count)
# Where
#   * `T` is a *known* numeric type, or a templated type
#   * `count` name resemble a size
#        (see LitgenOptions.fn_params_buffer_size_names__regex)

def add_inside_buffer(buffer: np.ndarray, number_to_add: int) -> None:
    """ add_inside_buffer: modifies a buffer by adding a value to its elements
     Will be published in python as:
     -->    def add_inside_buffer(buffer: np.ndarray, number_to_add: int) -> None:
     Warning, the python function will accept only uint8 numpy arrays, and check it at runtime!
    """
    pass

def buffer_sum(buffer: np.ndarray, stride: int = -1) -> int:
    """ buffer_sum: returns the sum of a *const* buffer
     Will be published in python as:
     -->    def buffer_sum(buffer: np.ndarray, stride: int = -1) -> int:
    """
    pass

def add_inside_two_buffers(
    buffer_1: np.ndarray,
    buffer_2: np.ndarray,
    number_to_add: int
    ) -> None:
    """ add_inside_two_buffers: modifies two mutable buffers
     litgen will detect that this function uses two buffers of same size.
     Will be published in python as:
     -->    def add_inside_two_buffers(buffer_1: np.ndarray, buffer_2: np.ndarray, number_to_add: int) -> None:
    """
    pass

def templated_mul_inside_buffer(buffer: np.ndarray, factor: float) -> None:
    """ templated_mul_inside_buffer: template function that modifies an array by multiplying its elements by a given factor
     litgen will detect that this function can be published as using a numpy array.
     It will be published in python as:
     -->    def mul_inside_buffer(buffer: np.ndarray, factor: float) -> None:

     The type will be detected at runtime and the correct template version will be called accordingly!
     An error will be thrown if the numpy array numeric type is not supported.
    """
    pass

#////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#                       mylib/c_string_list_test.h included by mylib/mylib.h                                   //
#//////////////////////////////////////////////////////////////////////////////////////////////////////////////


def c_string_list_total_size(
    items: List[str],
    output_0: BoxedInt,
    output_1: BoxedInt
    ) -> int:
    """ C String lists tests:
       Two consecutive params (const char *, int | size_t) are exported as List[str]

     The following function will be exported with the following python signature:
     -->    def c_string_list_total_size(items: List[str], output_0: BoxedInt, output_1: BoxedInt) -> int:
    """
    pass

#////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#                       mylib/modifiable_immutable_test.h included by mylib/mylib.h                            //
#//////////////////////////////////////////////////////////////////////////////////////////////////////////////


# Modifiable immutable python types test

# litgen adapts functions params that use modifiable pointer or reference to a type
# that is immutable in python.
# On the C++ side, these params are modifiable by the function.
# We need to box them into a Boxed type to ensure that any modification made by C++
# is visible when going back to Python.
#
# Note: immutable data types in python are
#   - Int, Float, String (correctly handled by litgen)
#   - Complex, Bytes (not handled)
#   - Tuple (not handled)


#///////////////////////////////////////////////////////////////////////////////////////////
# Test Part 1: in the functions below, the value parameters will be "Boxed"
#
# This is caused by the following options during generation:
#     options.fn_params_replace_modifiable_immutable_by_boxed__regex = code_utils.join_string_by_pipe_char([
#         r"^Toggle",
#         r"^Modify",
#      ])
#/////////////////////////////////////////////////////////////////////////////////////////


def toggle_bool_pointer(v: BoxedBool) -> None:
    """ Test with pointer:
     Will be published in python as:
     -->    def toggle_bool_pointer(v: BoxedBool) -> None:
    """
    pass

def toggle_bool_nullable(v: BoxedBool = None) -> None:
    """ Test with nullable pointer
     Will be published in python as:
     -->    def toggle_bool_nullable(v: BoxedBool = None) -> None:
    """
    pass

def toggle_bool_reference(v: BoxedBool) -> None:
    """ Test with reference
     Will be published in python as:
     -->    def toggle_bool_reference(v: BoxedBool) -> None:
    """
    pass

def modify_string(s: BoxedString) -> None:
    """ Test modifiable String
     Will be published in python as:
     -->    def modify_string(s: BoxedString) -> None:
    """
    pass


#///////////////////////////////////////////////////////////////////////////////////////////
#
# Test Part 2: in the functions below, the python return type is modified:
# the python functions will return a tuple:
#     (original_return_value, modified_parameter)
#
# This is caused by the following options during generation:
#
#     options.fn_params_output_modifiable_immutable_to_return__regex = r"^Change"
#/////////////////////////////////////////////////////////////////////////////////////////


def change_bool_int(label: str, value: int) -> Tuple[bool, int]:
    """ Test with int param + int return type
     Will be published in python as:
     --> def change_bool_int(label: str, value: int) -> Tuple[bool, int]:
    """
    pass

def change_void_int(label: str, value: int) -> int:
    """ Will be published in python as:
     -->    def change_void_int(label: str, value: int) -> int:
    """
    pass

def change_bool_int2(
    label: str,
    value1: int,
    value2: int
    ) -> Tuple[bool, int, int]:
    """ Will be published in python as:
     -->    def change_bool_int2(label: str, value1: int, value2: int) -> Tuple[bool, int, int]:
    """
    pass

def change_void_int_default_null(
    label: str,
    value: Optional[int] = None
    ) -> Tuple[bool, Optional[int]]:
    """ Will be published in python as:
     -->    def change_void_int_default_null(label: str, value: Optional[int] = None) -> Tuple[bool, Optional[int]]:
    """
    pass

def change_void_int_array(
    label: str,
    value: List[int]
    ) -> Tuple[bool, List[int]]:
    """ Will be published in python as:
     -->    def change_void_int_array(label: str, value: List[int]) -> Tuple[bool, List[int]]:
    """
    pass

#////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#                       mylib/overload_test.h included by mylib/mylib.h                                        //
#//////////////////////////////////////////////////////////////////////////////////////////////////////////////

# litgen is able to detect automatically the presence of overloads that require
# to use `py::overload_cast<...>` when publishing

# overload on free functions

def add_overload(a: int, b: int) -> int:  # type: ignore
    pass
def add_overload(a: int, b: int, c: int) -> int:  # type: ignore
    pass

# overload on methods

class FooOverload:
    def add_overload(self, a: int, b: int) -> int:          # type: ignore
        pass
    def add_overload(self, a: int, b: int, c: int) -> int:  # type: ignore
        pass


#For info, below is the generated C++ code that will publish these functions:
#
#     m.def("add_overload",
#        py::overload_cast<int, int>(add_overload), py::arg("a"), py::arg("b"));
#    m.def("add_overload",
#        py::overload_cast<int, int, int>(add_overload), py::arg("a"), py::arg("b"), py::arg("c"));
#
#
#    auto pyClassFooOverload = py::class_<FooOverload>
#        (m, "FooOverload", "")
#        .def(py::init<>()) // implicit default constructor
#        .def("add_overload",
#            py::overload_cast<int, int>(&FooOverload::add_overload), py::arg("a"), py::arg("b"))
#        .def("add_overload",
#            py::overload_cast<int, int, int>(&FooOverload::add_overload), py::arg("a"), py::arg("b"), py::arg("c"))
#        ;

#////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#                       mylib/enum_test.h included by mylib/mylib.h                                            //
#//////////////////////////////////////////////////////////////////////////////////////////////////////////////

class BasicEnum(Enum):
    """ BasicEnum: a simple C-style enum"""
    # C-style enums often contain a prefix that is the enum name in itself, in order
    # not to pollute the parent namespace.
    # Since enum members do not leak to the parent namespace in python, litgen will remove the prefix by default.

    a = auto()   # (= 1)  # This will be exported as BasicEnum.a
    aa = auto()  # (= 2)  # This will be exported as BasicEnum.aa
    aaa = auto() # (= 3)  # This will be exported as BasicEnum.aaa

    # Lonely comment

    # This is value b
    b = auto()   # (= 4)



# ClassEnumNotRegistered should not be published, as it misses the marker "// MY_API"
# By default, all enums, namespaces and classes are published,
# but you can decide to include only "marked" ones, via this litgen option:
#       options.srcml_options.api_suffixes = "MY_API"
#
# Note: Do not remove the empty line below, otherwise this comment would become part of
#       the enum's doc, and cause it to be registered (since it contains "MY_API")



class ClassEnum(Enum):
    """ ClassEnum: a class enum that should be published"""
    on = auto()      # (= 0)
    off = auto()     # (= 1)
    unknown = auto() # (= 2)


#For info, below is the python pyi stub that is published for this file:
#
#class BasicEnum(Enum):
#    """ BasicEnum: a simple C-style enum"""
#
#    a   # (= 1)  # This will be exported as BasicEnum.a
#    aa  # (= 2)  # This will be exported as BasicEnum.aa
#    aaa # (= 3)  # This will be exported as BasicEnum.aaa
#
#    # Lonely comment
#
#    # This is value b
#    b   # (= 4)
#
#    # This is c
#    # with doc on several lines
#    c   # (= BasicEnum.a | BasicEnum.b)
#
#
#class ClassEnum(Enum):
#    """ ClassEnum: a class enum that should be published"""
#    on      # (= 0)
#    off     # (= 1)
#    unknown # (= 2)

#////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#                       mylib/class_test.h included by mylib/mylib.h                                           //
#//////////////////////////////////////////////////////////////////////////////////////////////////////////////



class MyClass:
    """ This is the class doc. It will be published as MyClass.__doc__
     The "// MY_API" comment after the class decl indicates that this class will be published.
     it is necessary, since `options.srcml_options.api_suffixes = "MY_API"`
     was set inside autogenerate_mylib.py
    """
    def __init__(self, factor: int = 10, message: str = "hello") -> None:
        pass


    #/////////////////////////////////////////////////////////////////////////
    # Simple struct members
    #///////////////////////////////////////////////////////////////////////
    factor: int = 10
    delta: int = 0
    message: str


    #/////////////////////////////////////////////////////////////////////////
    # Stl container members
    #///////////////////////////////////////////////////////////////////////

    # By default, modifications from python are not propagated to C++ for stl containers
    # (see https://pybind11.readthedocs.io/en/stable/advanced/cast/stl.html)
    numbers: List[int]
    def append_number_from_cpp(self, v: int) -> None:
        """ However you can call dedicated modifying methods"""
        pass


    #/////////////////////////////////////////////////////////////////////////
    # Fixed size *numeric* array members
    #
    # They will be published as a py::array, and modifications will be propagated
    # on both sides transparently.
    #///////////////////////////////////////////////////////////////////////

    values: np.ndarray  # ndarray[type=int, size=2] default:{0, 1}
    flags: np.ndarray   # ndarray[type=bool, size=3] default:{False, True, False}


    #/////////////////////////////////////////////////////////////////////////
    # Simple methods
    #///////////////////////////////////////////////////////////////////////

    def calc(self, x: int) -> int:
        """ calc: example of simple method"""
        pass
    def set_message(self, m: str) -> None:
        """ set_message: another example of simple method"""
        pass


    #/////////////////////////////////////////////////////////////////////////
    # Static method
    #///////////////////////////////////////////////////////////////////////

    # (static method)
    def static_message() -> str:
        """ Returns a static message"""
        pass


# StructNotRegistered should not be published, as it misses the marker "// MY_API"
# By default, all enums, namespaces and classes are published,
# but you can decide to include only "marked" ones, via this litgen option:
#       options.srcml_options.api_suffixes = "MY_API"
#
# Note: Do not remove the empty line below, otherwise this comment would become part of
#       the enum's doc, and cause it to be registered (since it contains "MY_API")


#////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#                       mylib/return_value_policy_test.h included by mylib/mylib.h                             //
#//////////////////////////////////////////////////////////////////////////////////////////////////////////////

#
# return_value_policy:
#
# If a function has an end-of-line comment which contains `return_value_policy::reference`,
# and if this function returns a pointer or a reference, litgen will automatically add
# `pybind11::return_value_policy::reference` when publishing it.
#
# Note: `reference` could be replaced by `take_ownership`, or any other member of `pybind11::return_value_policy`


class MyConfig:
    # For example, singletons (such as the method below) should be returned as a reference,
    # otherwise python might destroy the singleton instance as soon as it goes out of scope.

    # (static method)
    def instance() -> MyConfig:
        """return_value_policy::reference"""
        pass

    value: int = 0

def my_config_instance() -> MyConfig:
    """return_value_policy::reference"""
    pass


#For info, below is the C++ generated binding code:
#
#     auto pyClassMyConfig = py::class_<MyConfig>
#        (m, "MyConfig", "")
#        .def(py::init<>()) // implicit default constructor
#        .def_readwrite("value", &MyConfig::value, "")
#        .def("instance",
#            &MyConfig::Instance,
#            " Instance() is a method that returns a pointer that should use `return_value_policy::reference`\nreturn_value_policy::reference",
#            pybind11::return_value_policy::reference)
#        ;
#
#
#    m.def("my_config_instance",
#        MyConfigInstance,
#        "return_value_policy::reference",
#        pybind11::return_value_policy::reference);

#////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#                       mylib/inner_class_test.h included by mylib/mylib.h                                     //
#//////////////////////////////////////////////////////////////////////////////////////////////////////////////


# namespace SomeNamespace

#////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#                       mylib/mix_adapters_class_test.h included by mylib/mylib.h                              //
#//////////////////////////////////////////////////////////////////////////////////////////////////////////////
# More complex tests, where we combine litgen function adapters with classes and namespace
#
# The main intent of these tests is to verify that the generated code compiles.
# The corresponding python test file will not test all these functions
# (as they are in fact copy/pasted/adapted from other tests)




#////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#                       mylib/namespace_test.h included by mylib/mylib.h                                       //
#//////////////////////////////////////////////////////////////////////////////////////////////////////////////


def foo_root() -> int:
    pass



"""MY_API This namespace should not be outputted as a submodule (it is considered a root namespace)"""




#////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#                       mylib/sandbox.h included by mylib/mylib.h                                              //
#//////////////////////////////////////////////////////////////////////////////////////////////////////////////
# Sandbox to play with litgen. Add some code here (with MY_API), and it will be exported

# <submodule SomeNamespace>
class SomeNamespace: # Proxy class that introduces typings for the *submodule* SomeNamespace
    # (This corresponds to a C++ namespace. All method are static!)
    class ParentStruct:
        class InnerStruct:
            value: int

            def __init__(self, value: int = 10) -> None:
                pass
            def add(self, a: int, b: int) -> int:
                pass

        class InnerEnum(Enum):
            zero = auto()  # (= 0)
            one = auto()   # (= 1)
            two = auto()   # (= 2)
            three = auto() # (= 3)

        inner_struct: InnerStruct
        inner_enum: InnerEnum = InnerEnum.three
    class Blah:
        """ struct Blah - MY_API"""
        def toggle_bool_pointer(self, v: BoxedBool) -> None:
            """//, int vv[2])"""
            pass

        def toggle_bool_pointer_get_points(
            self,
            v: BoxedBool,
            vv_0: BoxedInt,
            vv_1: BoxedInt
            ) -> None:
            pass


        def modify_string(self, s: BoxedString) -> None:
            pass



        def change_bool_int(self, label: str, value: int) -> Tuple[bool, int]:
            pass


        def add_inside_buffer(self, buffer: np.ndarray, number_to_add: int) -> None:
            pass

        def templated_mul_inside_buffer(
            self,
            buffer: np.ndarray,
            factor: float
            ) -> None:
            pass

        def const_array2_add(self, values: List[int]) -> int:
            pass

        def c_string_list_total_size(
            self,
            items: List[str],
            output_0: BoxedInt,
            output_1: BoxedInt
            ) -> int:
            pass





    # <submodule SomeInnerNamespace>
    class SomeInnerNamespace: # Proxy class that introduces typings for the *submodule* SomeInnerNamespace
        # (This corresponds to a C++ namespace. All method are static!)
        """ namespace SomeInnerNamespace - MY_API"""
        def toggle_bool_pointer(v: BoxedBool) -> None:
            """//, int vv[2])"""
            pass

        def toggle_bool_pointer_get_points(
            v: BoxedBool,
            vv_0: BoxedInt,
            vv_1: BoxedInt
            ) -> None:
            pass


        def modify_string(s: BoxedString) -> None:
            pass



        def change_bool_int(label: str, value: int) -> Tuple[bool, int]:
            pass


        def add_inside_buffer(buffer: np.ndarray, number_to_add: int) -> None:
            pass

        def templated_mul_inside_buffer(buffer: np.ndarray, factor: float) -> None:
            pass

        def const_array2_add(values: List[int]) -> int:
            pass

        def c_string_list_total_size(
            items: List[str],
            output_0: BoxedInt,
            output_1: BoxedInt
            ) -> int:
            pass


    # </submodule SomeInnerNamespace>

# </submodule SomeNamespace>

# <submodule Inner>
class Inner: # Proxy class that introduces typings for the *submodule* Inner
    # (This corresponds to a C++ namespace. All method are static!)
    """ this is an inner namespace (this comment should become the namespace doc)"""
    def foo_inner() -> int:
        pass
    def foo_inner2() -> int:
        pass

# </submodule Inner>
####################    </generated_from:mylib_amalgamation.h>    ####################

# </litgen_stub>
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!  AUTOGENERATED CODE END !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
