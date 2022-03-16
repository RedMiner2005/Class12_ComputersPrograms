"""Write a Python program to remove duplicates from a list 'a'
a = [10, 20, 30, 20, 10, 50, 60, 40, 80, 50, 40]


The textbook version uses two variables for some reason, but here it is:
a = [10, 20, 30, 20, 10, 50, 60, 40, 80, 50, 40]
duplicate, unique = [], []
for x in a:
    if x not in duplicate:
        unique.append(x)
        duplicate.append(x)
print(duplicate)
"""


a = [10, 20, 30, 20, 10, 50, 60, 40, 80, 50, 40]
print([a[i] for i in range(len(a)) if a[i] not in a[:i]])    # Or better yet, print(list(set(a))), but it destroys the order
