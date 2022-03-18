"""Example 11
Program to calculate thincome tax of an employee ont the basis of basic
salary and total savings inputted by the user (using nested if..else) as per:
1. No tax for individuals with incomes less than Rs. 2.5 lakh
2. 0% - 5% tax with income Rs. 2.5 lakh to Rs. 5 lakh for different age groups
3. 20% tax with income Rs. 5 lakh to Rs. 10 lakh
4. 30% tax with income greater than Rs. 10 lakh
5. Investments up to Rs. 1.5 lakh under Sec 80C can save up to Rs. 45000 in taxes
"""


basic = int(input("Enter the basic salary: "))
savings = int(input("Enter the total savings made: "))
if basic <= 250000:
    tax = 0
elif basic <= 500000:
    if savings > 150000:
        savings = 150000
    tot_income_5slab = 500000 - savings - 250000              # Total income under 5% slab
    tot_income_20slab = basic - 500000                        # Total income under 20% slab
    tax = tot_income_5slab * 0.05 + tot_income_20slab * 0.02  # 0.02 in textbook, isn't it 0.2?
else:
    if savings > 150000:
        savings = 150000
    tot_income_5slab = 500000 - savings - 250000              # Total income under 5% slab
    tot_income_30slab = basic - 1000000                       # Total income under 30% slab
    tax = (tot_income_5slab * 0.05 
        + tot_income_30slab * 0.03                            # 0.03 in textbook, isn't it 0.3?
        + 100000)                                             # 10000 is for 20% slab from 50000 to 1000000 tax calculated


print("Total income tax to be paid =", tax)
