"""Write a program to check if a string is a palindrome"""


txt = input("Please enter the string to be checked: ").lower()
print("It is {}a palindrome".format("" if txt == txt[::-1] else "not "))
