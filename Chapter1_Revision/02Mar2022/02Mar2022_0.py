"""Program on any topic from class 11th"""
"""
This program uses the sleep() function from the time module.
The purpose of this program is to show a simple animation in which the string 
stored in the variable named 'loading' is constructed and then destructed.
"""
from time import sleep


#############################
loading = "Hello World!"           # The string to be shown
wait = 0.5                         # The wait time between each step
#############################


while True:
    # The construction animation. i ranges from 0 to the length of the animation - 1, and the text is sliced accroding to i + 1
    for i in range(len(loading)):
        print(loading[:i+1], end="\r")   # The end value is a carriage return, returning the cursor to the beginning of the text
        sleep(wait)
    # The destruction animation. i ranges from the length of the string to 0, and the text is sliced according to i - 1
    for i in range(len(loading), 0, -1):
        print(loading[:i-1] + (" " * (len(loading) - i + 1)), end="\r")   # The end value is a carriage return, returning the cursor to the beginning of the text
        sleep(wait)
