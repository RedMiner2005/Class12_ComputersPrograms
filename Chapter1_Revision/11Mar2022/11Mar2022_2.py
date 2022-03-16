"""Input two numbers from the user and display their sum and product"""


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
print("Sum: {}\nProduct: {}".format(a + b, a * b))
