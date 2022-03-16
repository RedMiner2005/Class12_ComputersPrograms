"""Program to calculate and display the difference of 2 inputted numbers using if-else"""


def get_int(prompt: str):
    while True:
        num = input(prompt)
        try:
            num = int(num)
            break
        except ValueError as e:
            print("Please enter a valid integer.\n")
    return num


a = get_int("Please enter the first number: ")
b = get_int("Please enter the second number: ")

if a > b:
    print("The difference is:", a - b)
else:
    print("The difference is:", b - a)
