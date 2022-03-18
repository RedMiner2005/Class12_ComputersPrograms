"""Example 2 - pg2
Lokesh has taken a loan of Rs. 40000 from Vinod at an interest rate of 8% per annum.
After 6 years, he wants to repay the loan in full including interest.
Write the Python code (in script mode) to calculate and display the interest and total
amount to be paid by Lokesh to settle his accounts
"""


principal = 40000
rate = 8
time = 6

simple_int = principal * rate * time / 100
amount = principal + simple_int
print("Simple interest: Rs.", simple_int)
print("Amount payable: Rs.", amount)
