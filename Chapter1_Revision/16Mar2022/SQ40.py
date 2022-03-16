"""Write a Python program to remove the nth index character from a non-empty string"""


def remove_char(str, n):
    return str[:n] + str[n+1:]


if __name__ == "__main__":
    print(remove_char("Python", 0))
    print(remove_char("Python", 3))
    print(remove_char("Python", 5))
