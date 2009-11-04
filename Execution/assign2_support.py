#
# Support for assignment 2
#

# Imports for use in your assignment
from Tkinter import *
import tkMessageBox
from tkColorChooser import askcolor
from math import *


class FunctionError(Exception):
    """A simple function error exception produced by the make_function 
    function for invalid function definitions.
    """
    pass

def make_function(text):
    """Take a string representing a function in x and return the corresponding
    function.

    The FunctionError exception is thrown if text does not represent a valid
    function.

    make_function(string) -> (float -> float)
    """

    try:
        exec 'def f(x): return ' + text
        f(2)          ## test to see if there are any errors in the definition
    except ZeroDivisionError:  ## ignore zero division errors
        pass
    except:
        raise FunctionError()
    return f

