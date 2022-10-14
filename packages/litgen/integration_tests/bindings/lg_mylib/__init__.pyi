# type: ignore
import sys
from typing import Literal, List, Any, Optional, Tuple
import numpy as np
import enum
import numpy

# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!  AUTOGENERATED CODE !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# <litgen_stub> // Autogenerated code below! Do not edit!
####################    <generated_from:BoxedTypes>    ####################
class BoxedBool:
    value: bool
    def __init__(self, v: bool = False) -> None:
        pass
    def __repr__(self) -> str:
        pass
class BoxedInt:
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
class BoxedUnsignedLong:
    value: int
    def __init__(self, v: int = 0) -> None:
        pass
    def __repr__(self) -> str:
        pass
####################    </generated_from:BoxedTypes>    ####################


####################    <generated_from:mylib_amalgamation.h>    ####################
# THIS FILE WAS GENERATED AUTOMATICALLY. DO NOT EDIT.



#////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#                       mylib/basic_test.h included by mylib/mylib_main/mylib.h                                //
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



def my_generic_function(*args, **kwargs) -> int:
    """ This is a generic function for python, accepting (*args, **kwargs) as arguments"""
    pass




#////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#                       mylib/header_filter_test.h included by mylib/mylib_main/mylib.h                        //
#//////////////////////////////////////////////////////////////////////////////////////////////////////////////

# Here, we test that functions placed under unknown preprocessor conditions are not exported by default
# You could choose to add them anyway with:
#    options.srcmlcpp_options.header_filter_acceptable_suffixes += "|OBSCURE_OPTION"


#////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#                       mylib/c_style_array_test.h included by mylib/mylib_main/mylib.h                        //
#//////////////////////////////////////////////////////////////////////////////////////////////////////////////

#
# C Style array tests
#


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
#                       mylib/c_style_buffer_to_pyarray_test.h included by mylib/mylib_main/mylib.h            //
#//////////////////////////////////////////////////////////////////////////////////////////////////////////////


#
# C Style buffer to py::array tests
#
# litgen is able to recognize and transform pairs of params whose C++ signature resemble
#     (T* data, size_t|int count)
# Where
#   * `T` is a *known* numeric type, or a templated type
#   * `count` name resemble a size
#        (see LitgenOptions.fn_params_buffer_size_names__regex)
#

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
#                       mylib/c_string_list_test.h included by mylib/mylib_main/mylib.h                        //
#//////////////////////////////////////////////////////////////////////////////////////////////////////////////


def c_string_list_total_size(
    items: List[str],
    output_0: BoxedInt,
    output_1: BoxedInt
    ) -> int:
    """
     C String lists tests:
       Two consecutive params (const char *, int | size_t) are exported as List[str]

     The following function will be exported with the following python signature:
     -->    def c_string_list_total_size(items: List[str], output_0: BoxedInt, output_1: BoxedInt) -> int:

    """
    pass

#////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#                       mylib/modifiable_immutable_test.h included by mylib/mylib_main/mylib.h                 //
#//////////////////////////////////////////////////////////////////////////////////////////////////////////////


#
# Modifiable immutable python types test
#

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
#                       mylib/overload_test.h included by mylib/mylib_main/mylib.h                             //
#//////////////////////////////////////////////////////////////////////////////////////////////////////////////

#
# litgen is able to detect automatically the presence of overloads that require
# to use `py::overload_cast<...>` when publishing
#

#
# overload on free functions
#

def add_overload(a: int, b: int) -> int:  # type: ignore
    pass
def add_overload(a: int, b: int, c: int) -> int:  # type: ignore
    pass

#
# overload on methods
#

class FooOverload:
    def add_overload(self, a: int, b: int) -> int:          # type: ignore
        pass
    def add_overload(self, a: int, b: int, c: int) -> int:  # type: ignore
        pass

#////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#                       mylib/enum_test.h included by mylib/mylib_main/mylib.h                                 //
#//////////////////////////////////////////////////////////////////////////////////////////////////////////////

class BasicEnum(enum.Enum):
    """ BasicEnum: a simple C-style enum"""
    # C-style enums often contain a prefix that is the enum name in itself, in order
    # not to pollute the parent namespace.
    # Since enum members do not leak to the parent namespace in python, litgen will remove the prefix by default.

    a = enum.auto()   # (= 1)  # This will be exported as BasicEnum.a
    aa = enum.auto()  # (= 2)  # This will be exported as BasicEnum.aa
    aaa = enum.auto() # (= 3)  # This will be exported as BasicEnum.aaa

    # Lonely comment

    # This is value b
    b = enum.auto()   # (= 4)



class ClassEnum(enum.Enum):
    """ ClassEnum: a class enum that should be published"""
    on = enum.auto()      # (= 0)
    off = enum.auto()     # (= 1)
    unknown = enum.auto() # (= 2)



#////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#                       mylib/class_test.h included by mylib/mylib_main/mylib.h                                //
#//////////////////////////////////////////////////////////////////////////////////////////////////////////////



class MyClass:
    """ This is the class doc. It will be published as MyClass.__doc__"""
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

    values: np.ndarray            # ndarray[type=int, size=2] default:{0, 1}
    flags: np.ndarray             # ndarray[type=bool, size=3] default:{False, True, False}

    const_static_value: int = 101 # (C++ static member)
    static_value: int             # (C++ static member)

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




class MySingletonClass:
    """ MySingletonClass: demonstrate how to instantiate a singleton
     - The instance method shall return with return_value_policy::reference
     - The destructor may be private
    """
    value: int = 0

    # (static method)
    def instance() -> MySingletonClass:
        """return_value_policy::reference"""
        pass




class MyFinalClass:
    """ This struct is final, and thus cannot be inherited from python
    (final class)
    """
    def foo(self) -> int:
        pass


class MyStructDynamic:
    """ This class accepts dynamic attributes
     see autogenerate_mylib.py:
         options.class_dynamic_attributes__regex = r"Dynamic$"
    """
    cpp_member: int = 1

#////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#                       mylib/class_inheritance_test.h included by mylib/mylib_main/mylib.h                    //
#//////////////////////////////////////////////////////////////////////////////////////////////////////////////





def make_dog() -> Animals.Animal:
    """ Test that downcasting works: the return type is Animal, but it should bark!"""
    pass

#////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#                       mylib/class_adapt_test.h included by mylib/mylib_main/mylib.h                          //
#//////////////////////////////////////////////////////////////////////////////////////////////////////////////


class Color4:
    def __init__(self, _rgba: List[int]) -> None:
        """ The constructor params will automatically be "adapted" into std::array<uint8_t, 4>"""
        pass

    # This member will be stored as a modifiable numpy array
    rgba: np.ndarray  # ndarray[type=uint8_t, size=4]

#////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#                       mylib/class_copy_test.h included by mylib/mylib_main/mylib.h                           //
#//////////////////////////////////////////////////////////////////////////////////////////////////////////////


class Copyable_ImplicitCopyCtor:
    a: int = 1


class Copyable_ExplicitCopyCtor:
    def __init__(self) -> None:
        pass
    def __init__(self, other: Copyable_ExplicitCopyCtor) -> None:
        pass
    a: int = 1


class Copyable_ExplicitPrivateCopyCtor:
    def __init__(self) -> None:
        pass
    a: int = 1



class Copyable_DeletedCopyCtor:
    a: int = 1
    def __init__(self, : Copyable_DeletedCopyCtor) -> None:
        pass

#////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#                       mylib/class_virtual_test.h included by mylib/mylib_main/mylib.h                        //
#//////////////////////////////////////////////////////////////////////////////////////////////////////////////


#
#This test will exercise the following options:
#
#    # class_expose_protected_methods__regex:
#    # regex giving the list of class names for which we want to expose protected methods.
#    # (by default, only public methods are exposed)
#    # If set, this will use the technique described at
#    # https://pybind11.readthedocs.io/en/stable/advanced/classes.html#binding-protected-member-functions)
#    class_expose_protected_methods__regex: str = ""
#
#    # class_expose_protected_methods__regex:
#    # regex giving the list of class names for which we want to be able to override virtual methods
#    # from python.
#    # (by default, this is not possible)
#    # If set, this will use the technique described at
#    # https://pybind11.readthedocs.io/en/stable/advanced/classes.html#overriding-virtual-functions-in-python
#    #
#    # Note: if you want to override protected functions, also fill `class_expose_protected_methods__regex`
#    class_override_virtual_methods_in_python__regex: str = ""
#


#////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#                       mylib/return_value_policy_test.h included by mylib/mylib_main/mylib.h                  //
#//////////////////////////////////////////////////////////////////////////////////////////////////////////////

#
# return_value_policy:
#
# If a function has an end-of-line comment which contains `return_value_policy::reference`,
# and if this function returns a pointer or a reference, litgen will automatically add
# `pybind11::return_value_policy::reference` when publishing it.
#
# Notes: `reference` could be replaced by `take_ownership`, or any other member of `pybind11::return_value_policy`
#
# You can also set a global options for matching functions names that return a reference or a pointer
#     see
#             LitgenOptions.fn_return_force_policy_reference_for_pointers__regex
#     and
#             LitgenOptions.fn_return_force_policy_reference_for_references__regex: str = ""


class MyConfig:
    #
    # For example, singletons (such as the method below) should be returned as a reference,
    # otherwise python might destroy the singleton instance as soon as it goes out of scope.
    #

    # (static method)
    def instance() -> MyConfig:
        """return_value_policy::reference"""
        pass

    value: int = 0

def my_config_instance() -> MyConfig:
    """return_value_policy::reference"""
    pass

#////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#                       mylib/inner_class_test.h included by mylib/mylib_main/mylib.h                          //
#//////////////////////////////////////////////////////////////////////////////////////////////////////////////



#////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#                       mylib/mix_adapters_class_test.h included by mylib/mylib_main/mylib.h                   //
#//////////////////////////////////////////////////////////////////////////////////////////////////////////////
# More complex tests, where we combine litgen function adapters with classes and namespace
#
# The main intent of these tests is to verify that the generated code compiles.
# The corresponding python test file will not test all these functions
# (as they are in fact copy/pasted/adapted from other tests)
#




#////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#                       mylib/namespace_test.h included by mylib/mylib_main/mylib.h                            //
#//////////////////////////////////////////////////////////////////////////////////////////////////////////////


def foo_root() -> int:
    pass



"""MY_API This namespace should not be outputted as a submodule (it is considered a root namespace)"""



#////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#                       mylib/operators.h included by mylib/mylib_main/mylib.h                                 //
#//////////////////////////////////////////////////////////////////////////////////////////////////////////////

class IntWrapper:
    value: int
    def __init__(self, v: int) -> None:
        pass

    # arithmetic operators
    def __add__(self, b: IntWrapper) -> IntWrapper:
        pass
    def __sub__(self, b: IntWrapper) -> IntWrapper:
        pass

    def __neg__(self) -> IntWrapper:
        """ Unary minus operator"""
        pass

    def __lt__(self, b: IntWrapper) -> bool:
        """ Comparison operator"""
        pass

    # Two overload of the += operator
    def __iadd__(self, b: IntWrapper) -> IntWrapper:
        pass
    def __iadd__(self, b: int) -> IntWrapper:
        pass

    # Two overload of the call operator, with different results
    def __call__(self, b: IntWrapper) -> int:
        pass
    def __call__(self, b: int) -> int:
        pass


class IntWrapperSpaceship:
    value: int

    def __init__(self, v: int) -> None:
        pass

    # Test spaceship operator, which will be split into 5 operators in Python!
    # ( <, <=, ==, >=, >)
    # Since we have two overloads, 10 python methods will be built
    def __lt__(self, o: IntWrapperSpaceship) -> bool:
        pass
    def __le__(self, o: IntWrapperSpaceship) -> bool:
        pass
    def __eq__(self, o: IntWrapperSpaceship) -> bool:
        pass
    def __ge__(self, o: IntWrapperSpaceship) -> bool:
        pass
    def __gt__(self, o: IntWrapperSpaceship) -> bool:
        pass
    def __lt__(self, o: int) -> bool:
        pass
    def __le__(self, o: int) -> bool:
        pass
    def __eq__(self, o: int) -> bool:
        pass
    def __ge__(self, o: int) -> bool:
        pass
    def __gt__(self, o: int) -> bool:
        pass

#////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#                       mylib/call_policies_test.h included by mylib/mylib_main/mylib.h                        //
#//////////////////////////////////////////////////////////////////////////////////////////////////////////////




# ============================================================================
# call_guard
# ============================================================================
# If you add a comment to the function with reads:
#     py::call_guard<YourCallGuard>()
# Then, it will be taken into account
# See https://pybind11.readthedocs.io/en/stable/advanced/functions.html#call-guard
# The comment may be a comment on previous line or an end-of-line comment

def call_guard_tester() -> None:
    """// py::call_guard<CallGuardLogger>()"""
    pass


# ============================================================================
# keep-alive
# ============================================================================
# If you add a comment to the function with reads:
#     py::keep-alive<1, 2>()
# Then, it will be taken into account
# See https://pybind11.readthedocs.io/en/stable/advanced/functions.html#keep-alive
# The comment may be a comment on previous line or an end-of-line comment
#
# (No integration test implemented for this)


# ============================================================================
# return value policy
# => see doc inside return_value_policy_test.h
# ============================================================================


class CallGuardLogger:
    """ ============================================================================
     CallGuardLogger: dummy call guard for the tests
     ============================================================================
    """
    def __init__(self) -> None:
        pass

    nb_construct: int # (C++ static member)
    nb_destroy: int   # (C++ static member)


#////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#                       mylib/template_function_test.h included by mylib/mylib_main/mylib.h                    //
#//////////////////////////////////////////////////////////////////////////////////////////////////////////////


# AddTemplated is a template function that will be implemented for the types ["int", "double", "std::string"]
#
# See inside autogenerate_mylib.py:
#     options.fn_template_options.add_specialization(r"^AddTemplated$", ["int", "double", "std::string"])

#  ------------------------------------------------------------------------
#      <template specializations for function AddTemplated>
def add_templated(a: int, b: int) -> int:
    pass


def add_templated(a: float, b: float) -> float:
    pass


def add_templated(a: str, b: str) -> str:
    pass
#      </template specializations for function AddTemplated>
#  ------------------------------------------------------------------------


# SumVectorAndCArray is a template function that will be implemented for the types ["int", "std::string"]
#
# Here, we test two additional thing:
#  - nesting of the T template parameter into a vector
#  - mixing template and function parameter adaptations (here other_values[2] will be transformed into a List[T]
#
# See inside autogenerate_mylib.py:
#     options.fn_template_options.add_specialization(r"^SumVector", ["int", "std::string"])

#  ------------------------------------------------------------------------
#      <template specializations for function SumVectorAndCArray>
def sum_vector_and_c_array(xs: List[int], other_values: List[int]) -> int:
    pass


def sum_vector_and_c_array(xs: List[str], other_values: List[str]) -> str:
    pass
#      </template specializations for function SumVectorAndCArray>
#  ------------------------------------------------------------------------


# Same test, as a method

class FooTemplateFunctionTest:
    #  ------------------------------------------------------------------------
    #      <template specializations for function SumVectorAndCArray>
    def sum_vector_and_c_array(
        self,
        xs: List[int],
        other_values: List[int]
        ) -> int:
        pass

    def sum_vector_and_c_array(
        self,
        xs: List[str],
        other_values: List[str]
        ) -> str:
        pass
    #      </template specializations for function SumVectorAndCArray>
    #  ------------------------------------------------------------------------

#////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#                       mylib/template_class_test.h included by mylib/mylib_main/mylib.h                       //
#//////////////////////////////////////////////////////////////////////////////////////////////////////////////


#  MyTemplateClass is a template class that will be implemented for the types ["int", "std::string"]
#
# See inside autogenerate_mylib.py:
#        options.class_template_options.add_specialization(
#            class_name_regex=r"^MyTemplateClass$",  # r".*" => all classes
#        cpp_types_list=["int", "double"],  # instantiated types
#        naming_scheme=litgen.TemplateNamingScheme.camel_case_suffix,
#        )

#  ------------------------------------------------------------------------
#      <template specializations for class MyTemplateClass>
class MyTemplateClassInt:
    values: List[int]

    def __init__(self) -> None:
        """ Standard constructor"""
        pass

    def __init__(self, v: List[int]) -> None:
        """ Constructor that will need a parameter adaptation"""
        pass

    def sum(self) -> int:
        """ Standard method"""
        pass

    def sum2(self, v: List[int]) -> int:
        """ Method that requires a parameter adaptation"""
        pass


class MyTemplateClassString:
    values: List[str]

    def __init__(self) -> None:
        """ Standard constructor"""
        pass

    def __init__(self, v: List[str]) -> None:
        """ Constructor that will need a parameter adaptation"""
        pass

    def sum(self) -> str:
        """ Standard method"""
        pass

    def sum2(self, v: List[str]) -> str:
        """ Method that requires a parameter adaptation"""
        pass
#      </template specializations for class MyTemplateClass>
#  ------------------------------------------------------------------------


#////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#                       mylib/mylib_main/mylib.h continued                                                     //
#//////////////////////////////////////////////////////////////////////////////////////////////////////////////

##include "mylib/sandbox.h"

# <submodule MathFunctions>
class MathFunctions:  # Proxy class that introduces typings for the *submodule* MathFunctions
    pass  # (This corresponds to a C++ namespace. All method are static!)
    """ Vectorizable functions example
        Numeric functions (i.e. function accepting and returning only numeric params or py::array), can be vectorized
        i.e. they will accept numpy arrays as an input.

     Auto-vectorization is enabled via the following options:
         options.fn_namespace_vectorize__regex: str = r"^MathFunctions$"
         options.fn_vectorize__regex = r".*"

    """
    def vectorizable_sum(x: float, y: float) -> float:
        pass
    def vectorizable_sum(x: np.ndarray, y: np.ndarray) -> np.ndarray:
        pass

# </submodule MathFunctions>

# <submodule Animals>
class Animals:  # Proxy class that introduces typings for the *submodule* Animals
    pass  # (This corresponds to a C++ namespace. All method are static!)
    class Animal:
        def __init__(self, name: str) -> None:
            pass
        name: str


    class Dog(Animals.Animal):
        def __init__(self, name: str) -> None:
            pass
        def bark(self) -> str:
            pass



# </submodule Animals>

# <submodule Home>
class Home:  # Proxy class that introduces typings for the *submodule* Home
    pass  # (This corresponds to a C++ namespace. All method are static!)
    class Pet:
        def is_pet(self) -> bool:
            pass

    class PetDog(Animals.Dog, Home.Pet):
        def __init__(self, name: str) -> None:
            pass
        def bark(self) -> str:
            pass



# </submodule Home>

# <submodule Root>
class Root:  # Proxy class that introduces typings for the *submodule* Root
    pass  # (This corresponds to a C++ namespace. All method are static!)

    # <submodule Inner>
    class Inner:  # Proxy class that introduces typings for the *submodule* Inner
        pass  # (This corresponds to a C++ namespace. All method are static!)
        class MyVirtualClass:

            def foo_concrete(self, x: int, name: str) -> str:
                pass

            def foo_virtual_public_pure(self) -> int:                      # overridable (pure virtual)
                pass

            # <protected_methods>
            def foo_virtual_protected(self, x: int) -> int:                # overridable
                pass
            def foo_virtual_protected_const_const(self, name: str) -> str: # overridable
                pass
            # </protected_methods>


        class MyVirtualDerivate(Root.Inner.MyVirtualClass):
            """ Here, we test Combining virtual functions and inheritance
             See https://pybind11.readthedocs.io/en/stable/advanced/classes.html#combining-virtual-functions-and-inheritance
            """
            def __init__(self) -> None:
                pass
            def foo_virtual_public_pure(self) -> int: # overridable
                pass
            def foo_derivate(self) -> int:            # overridable
                pass

    # </submodule Inner>

# </submodule Root>

# <submodule SomeNamespace>
class SomeNamespace:  # Proxy class that introduces typings for the *submodule* SomeNamespace
    pass  # (This corresponds to a C++ namespace. All method are static!)
    """ namespace SomeNamespace"""
    class ParentStruct:
        class InnerStruct:
            value: int

            def __init__(self, value: int = 10) -> None:
                pass
            def add(self, a: int, b: int) -> int:
                pass

        class InnerEnum(enum.Enum):
            zero = enum.auto()  # (= 0)
            one = enum.auto()   # (= 1)
            two = enum.auto()   # (= 2)
            three = enum.auto() # (= 3)

        inner_struct: InnerStruct
        inner_enum: InnerEnum = InnerEnum.three
    class Blah:
        """ struct Blah"""
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
    class SomeInnerNamespace:  # Proxy class that introduces typings for the *submodule* SomeInnerNamespace
        pass  # (This corresponds to a C++ namespace. All method are static!)
        """ namespace SomeInnerNamespace"""
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
class Inner:  # Proxy class that introduces typings for the *submodule* Inner
    pass  # (This corresponds to a C++ namespace. All method are static!)
    """ this is an inner namespace (this comment should become the namespace doc)"""
    def foo_inner() -> int:
        pass
    def foo_inner2() -> int:
        pass

# </submodule Inner>
####################    </generated_from:mylib_amalgamation.h>    ####################

# </litgen_stub>
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!  AUTOGENERATED CODE END !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
