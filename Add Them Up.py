"""
Using split() method :
This function helps in getting a multiple inputs from user.
It breaks the given input by the specified separator.
If a separator is not provided then any white space is a separator.
Generally, user use a split() method to split a Python string but one can use it in taking multiple input.

Syntax :
input().split(separator, maxsplit)
example:
link:https://www.geeksforgeeks.org/taking-multiple-inputs-from-user-in-python/?ref=rp
"""

A, B = [int(A) for A in input().split()]
s = A+ B
print(s)