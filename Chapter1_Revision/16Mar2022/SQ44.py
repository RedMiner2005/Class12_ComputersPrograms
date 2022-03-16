"""
IMPORTANT!?
It's not working properly (for the second example), it looks as if it's just rounding it off. (This is the textbook version)

Write a Python program to print the following floating point numbers with no decimal places.
x = 3.1415926
y = -12.9999
"""


def formatter(number: float):
    print("Original number: ", number)
    print("Formatted number with no decimal places: " + "{:.0f}".format(number))


x = 3.1415926
y = -12.9999
formatter(x)
formatter(y)
