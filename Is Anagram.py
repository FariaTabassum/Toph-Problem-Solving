"""
The sorted() function returns a sorted list of the specified iterable object.
You can specify ascending or descending order. Strings are sorted alphabetically,
and numbers are sorted numerically.
Note: You cannot sort a list that contains BOTH string values AND numeric values.
"""
s1 = input()
s2 = input()
if (sorted(s1)== sorted(s2)):
    print("Yes")
else:
    print("No")