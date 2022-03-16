"""Write a program to calculate simple interest and amount payable by
inputting the rate and principal amount for a period of 5 years."""


def get_float(prompt: str):
    while True:
        num = input(prompt)
        try:
            num = float(num)
            break
        except ValueError as e:
            print("Please enter a valid integer.\n")
    return num


print("This program calculates simple interest and the amount payable after 5 years.\n")

time = 5
principal = get_float("Please enter the principal value: ")
rate = get_float("Please enter the percentage rate of interest (per annum): ")

interest = principal * rate * time / 100
print(f"Interest after 5 years: {interest}\nAmount Payable: {principal + interest}")
