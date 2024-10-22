# ============================================================================
# This file was autogenerated
# It is presented side to side with its source: class_test.h
#    (see integration_tests/bindings/lg_mylib/__init__pyi which contains the full
#     stub code, including this code)
# ============================================================================

# type: ignore
# ruff: noqa: F821

from typing import List
import numpy as np
import enum

# <litgen_stub> // Autogenerated code below! Do not edit!
####################    <generated_from:class_test.h>    ####################

class MyClass:
    """This is the class doc. It will be published as MyClass.__doc__"""

    def __init__(self, factor: int = 10, message: str = "hello") -> None:
        pass
    # /////////////////////////////////////////////////////////////////////////
    # Simple struct members
    # ///////////////////////////////////////////////////////////////////////
    factor: int = 10
    delta: int = 0
    message: str

    # /////////////////////////////////////////////////////////////////////////
    # Stl container members
    # ///////////////////////////////////////////////////////////////////////

    # By default, modifications from python are not propagated to C++ for stl containers
    # (see https://pybind11.readthedocs.io/en/stable/advanced/cast/stl.html)
    numbers: List[int]
    def append_number_from_cpp(self, v: int) -> None:
        """However you can call dedicated modifying methods"""
        pass
    # /////////////////////////////////////////////////////////////////////////
    # Fixed size *numeric* array members
    #
    # They will be published as a py::array, and modifications will be propagated
    # on both sides transparently.
    # ///////////////////////////////////////////////////////////////////////

    values: np.ndarray  # ndarray[type=int, size=2] default:int(0, 1)
    flags: np.ndarray  # ndarray[type=bool, size=3] default:bool(False, True, False)

    const_static_value: int = 101  # (C++ static member) # (const)
    static_value: int  # (C++ static member)

    # /////////////////////////////////////////////////////////////////////////
    # Simple methods
    # ///////////////////////////////////////////////////////////////////////

    def calc(self, x: int) -> int:
        """calc: example of simple method"""
        pass
    def set_message(self, m: str) -> None:
        """set_message: another example of simple method"""
        pass
    # /////////////////////////////////////////////////////////////////////////
    # Static method
    # ///////////////////////////////////////////////////////////////////////

    @staticmethod
    def static_message() -> str:
        """Returns a static message"""
        pass

class MySingletonClass:
    """MySingletonClass: demonstrate how to instantiate a singleton
    - The instance method shall return with return_value_policy::reference
    - The destructor may be private
    """

    value: int = 0
    def __init__(self) -> None:
        pass
    @staticmethod
    def instance() -> MySingletonClass:
        """py::return_value_policy::reference"""
        pass

class MyFinalClass:
    """This struct is final, and thus cannot be inherited from python
    (final class)
    """

    def foo(self) -> int:
        pass
    def __init__(self) -> None:
        """Auto-generated default constructor"""
        pass

class MyStructDynamic:
    """This class accepts dynamic attributes
    see autogenerate_mylib.py:
        options.class_dynamic_attributes__regex = r"Dynamic$"
    """

    cpp_member: int = 1
    def __init__(self, cpp_member: int = 1) -> None:
        """Auto-generated default constructor with named params"""
        pass

class MyStructWithNestedEnum:
    class Choice(enum.Enum):
        a = enum.auto()  # (= 0)
    def handle_choice(
        self, value: MyStructWithNestedEnum.Choice = MyStructWithNestedEnum.Choice.a
    ) -> int:
        """The first param of this function uses the inner scope of this class!
        When building the bindings, we need to add MyStructWithNestedEnum::
        """
        pass
    def __init__(self) -> None:
        """Auto-generated default constructor"""
        pass

####################    </generated_from:class_test.h>    ####################

# </litgen_stub> // Autogenerated code end!
