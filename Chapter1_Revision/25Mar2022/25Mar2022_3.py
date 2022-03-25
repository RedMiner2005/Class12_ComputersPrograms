"""Write a program that calculates any of the following depending on the option the user chooses
1. Area of a cicle
2. Circumference of a circle
3. Area of a rectangle
4. Area of a square
"""


def get_inputs(params):
    results = []
    for param in params:
        while True:
            try:
                results.append(int(input(f"Please enter the value of '{param}': ")))
                break
            except ValueError as e:
                print("Please enter a valid integer.\n")
    return results


def get_choice(options):
    display_list = "\n".join(map(lambda x: f"{x[0]}. {x[1]}", enumerate(options, start=1)))
    while True:
        print("Please choose an item from the following:\n{}".format(display_list))
        try:
            opt = int(input("Enter your choice: "))
            assert 1 <= opt <= len(options)
            break
        except Exception as e:
            print("Please enter a valid integer from 1 to", len(options), end="\n\n")
    return opt


def main():
    menu_items = (
        ("Area of a circle", ("radius",), lambda r: 3.14*r*r),
        ("Circumference of a circle", ("radius",), lambda r: 6.28*r),
        ("Area of a rectangle", ("length", "breadth"), lambda l, b: l*b),
        ("Area of a square", ("side",), lambda a: a*a),
    )
    zipped = tuple(zip(*menu_items))
    option = get_choice(zipped[0]) - 1
    inputs = get_inputs(zipped[1][option])
    print("The answer is:", zipped[2][option](*inputs))


if __name__ == "__main__":
    main()
