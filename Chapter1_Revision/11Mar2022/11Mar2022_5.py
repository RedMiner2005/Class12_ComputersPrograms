"""Program to calculate the area of a circle"""


def get_float(prompt: str):
    while True:
        num = input(prompt)
        try:
            num = float(num)
            break
        except ValueError as e:
            print("Please enter a valid integer.\n")
    return num


radius = get_float("Enter the radius of the circle: ")
print(f"Area of the circle with radius {radius} is: {3.14 * radius * radius}")
