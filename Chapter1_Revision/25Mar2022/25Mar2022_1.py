"""Get all the prime numbers from 2 to n"""
from time import time


# Get a valid integer
while True:
    try:
        n = int(input("Enter the upper limit of the range: "))
        break
    except ValueError as e:
        print("Please enter a valid integer.\n")


# Calculate all the multiples and then remove them from the range of numbers from 2 to n
init = time()
primes = set(range(2, n)).difference(*[set(range(2*i, i * n//i, i)) for i in range(2, n)])
final = time()
print(", ".join(map(str, primes)))
print("Time:", final-init)
