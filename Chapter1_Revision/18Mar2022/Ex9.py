"""Example 9
Program to calculate and display the difference of two inputted numbers
"""


num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
if num1 > num2:
    diff = num1 - num2
else:
    diff = num2 - num1
print(f"The difference of {num1} and {num2}: {diff}")
