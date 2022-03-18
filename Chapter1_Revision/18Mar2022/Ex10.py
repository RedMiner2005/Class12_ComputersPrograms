"""Example 10
Program to illustrate nested if else through a four function calculator
"""


result = 0
val1 = float(input("Enter value 1: "))
val2 = float(input("Enter value 2: "))
op = input("Enter the any operator (from +, -, *, /): ")

if op == "+":
    result = val1 + val2
elif op == "-":
    if val1 > val2:
        result = val1 - val2
    else:
        result = val2 - val1
elif op == "*":
    result = val1 * val2
elif op == "/":
    if val2 == 0:
        print("Please enter a value other than 0.")
    else:
        result = val1 / val2
else:
    print("Please enter a valid operator.")

print("Result is:", result)