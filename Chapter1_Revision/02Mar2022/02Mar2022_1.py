"""A program based on user-defined functions"""
"""
This program has a custom-defined function to repeatedly ask for an integer until a vlid integer is inputted
"""


def get_int(prompt):
    while True:
        num = input(prompt)
        try:
            return int(num)
        except ValueError:
            print("Please enter a valid integer.\n")
            continue


def main():
    n1 = get_int("Enter the first number: ")
    n2 = get_int("Enter the second number: ")
    n3 = get_int("Enter the third number: ")
    print("The largest number is:", max((n1, n2, n3)))


if __name__ == "__main__":
    main()
