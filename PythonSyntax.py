#! /usr/bin/env python

# -*- coding: ascii -*-

# import examples
# from lib import x # similar to a static import in java, referenced with x()
# from lib import x as y # similar to a static import in java, but can be referenced with y()

from my_python_library import utils

# import lib # non-static import, best, as it is visible where library came from, referenced as lib.x()


"""
reference: dzone refcard core python
"""


def conditional_logic(something_is_true, something_else_is_true):
    """
    Python has a very straightforward set of if/else statements
    Python does not have a switch statement.
    """
    if something_is_true:
        # do this
        print "do this"
    elif something_else_is_true:
        # do that
        print "do that"
    else:
        # do the other thing
        print "do the other thing"


def loops():
    # for loops
    for item in ['spam', 'spam', 'spam', 'spam']:
        print item

    for i in range(5):
        print i  # Prints numbers from 0 to 4

    for i in range(4, 10):
        print i  # Prints numbers 4, 5, 6, 7, 8, 9

    for i in range(4, 10, 2):
        print i  # Prints numbers 4, 6, 8

    # while loops
    countdown = 10
    while countdown > 0:
        print countdown
        countdown -= 1

loops()


def do_something_that_could_raise_exception(var):
    try:
        item = var[0]
    except TypeError:
        # this will print only on a TypeError exception
        print "x isn't a list!"
    else:
        # executes if the code in the "try" does NOT raise an exception
        print "You didn't raise an exception!"
    finally:
        # this will always print
        print "processing complete"


my_list = [1, 2]
do_something_that_could_raise_exception(my_list)

# data types
int      #
long     #
float    #
complex  #
bool     #

# object types
list     # Mutable sequence, always in square brackets: [1, 2, 3]
tuple    # Immutable sequence, always in parentheses: (a, b, c)
dict     # Dictionary - key, value storage. Uses curly braces: {key:value}
set      # Collection of unique elements unordered, no duplicates
str      # String - sequence of characters, immutable
unicode  # Sequence of Unicode encoded characters

# SEQUENCE INDEXES AND SLICING

x = [0, 1, 2, 3]
print(x[0])     # returns element at index 0
print(x[1])     # returns element at index 1
print(x[-1])    # returns last element of sequence
print(x[1:])    # second element through last element
print(x[:-1])   # First element up to (but NOT including last element)
print(x[:])     # returns all elements of list, copy of list
print(x[0::2])  # starts at the first element, then every 2nd element

# working with tuples and maps
dictionary = {'key1': 5, 'key2': 12}
for k, v in dictionary.items():
    print(k, v)


# Strings
s = "joey faherty"
print(s[:])
print(s[5:])
print(s[1:3])

# print("The ultimate answer is: " + 42) # Will cause a runtime error
print("The ultimate answer is: " + str(42)) # converts the int to a string


print("Nice to meet you {}.".format("Joey"))


def multi_args(*args):
    # here args is a tuple
    print(args)

multi_args(1, 2, 3, 4, 5)


def multi_args_kv(**args):
    # here args is a dictionary:
    print(args)

multi_args_kv(hello=1, b=2, c=3)


def returns_a_string():
    return "help"

returns_a_string()


def returns_a_tuple():
    return 7, 5, 9

seven, five, nine = returns_a_tuple()
print(seven, five, nine)


class MyClass(object):
    def __init__(self, par):
        # initialize some stuff
        self.foo = "bar"

    def a_method(self):
        # do something
        print "hello"

    def another_method(self, parameter):
        # do something with parameter
        print parameter


# imports an internal library/class from the my_python_library package
sum_result = utils.sum_function(1, 9)
print(sum_result)
"""
Notice that to turn my_library into a Python library we need to put an empty __init__.py file in it. 
Otherwise Python won’t import modules from a directory.
"""


# Be aware that when a module is imported, its code is executed.
# Therefore, if you want a module to contain an entry point to your application,
# it is recommended to add the following if statement to it:
def foo(a, b):
    return a + b
if __name__ == "__main__":
    # Application logic goes here
    print("we are now running app code")


class Restaurant(object):
    """
    Indentation is essential. Best practice is 4 space indentation per level
    no braces required.
    """
    # this is another one-line comment
    bankrupt = False

    def open_branch(self):
        if not self.bankrupt:
            print("branch opened")

x = Restaurant()
Restaurant.open_branch(x)