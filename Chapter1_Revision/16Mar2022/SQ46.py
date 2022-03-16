"""Write a Python program to print the index of the character in a string

Sample string: Python Program
Sample output:
Current character P position at 0
Current character y position at 1
Current character t position at 2
... and so on
"""


text = input("Enter the string: ")
for i, char in enumerate(text):
    print(f"Current character {char} position at {i}")
