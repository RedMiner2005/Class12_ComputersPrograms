"""Example 6
Write a Python code to calculate simple interest and amount payable by inputting
the value of principal amount and rate from the user for a time period of five years.
"""

principal = eval(input("Enter the value of principal: "))
rate = eval(input("Enter the annual rate of interest: "))
time = 5

simple_int = principal * rate * time / 100
amount = principal + simple_int
print("Simple Interest:", simple_int)
print("Amount Payable:", amount)
