"""Write a Python program that accepts a comma-separated sequence of words as input 
and prints the unique words in sorted form (alphanumeric)
Sample Words: red, white, black, red, green, black
Expected Result: black, green, red, white

Textbook version:
items = input(": ")
words = [word for word in items.split(",")]
print(", ".join(sorted(list(set(words)))))


My Oneliner Version
"""


print(", ".join(
        sorted(set(
            input("Please enter the comma separated list of values: ").replace(" ", "").split(",")
        ))
    ))

