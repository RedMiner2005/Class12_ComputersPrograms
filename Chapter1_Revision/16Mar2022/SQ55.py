"""Write a Python program to count the number of elements in a list within a specified range.

The textbook version overrides functions like min and max, so the variable names are changed.
It is also very weird. It only works if the elements are sorted because start and stop are 
not index values, they are actual values of the elements.

Textbook version
"""


def count_range_in_list(data, start, stop):
    counter = 0
    for x in data:
        if start <= x <= stop:
            counter += 1
    return counter


list1 = [10, 20, 30, 40, 40, 40, 70, 80, 99]
print(count_range_in_list(list1, 40, 100))
list2 = ['a', 'b', 'c', 'd', 'e', 'f']
print(count_range_in_list(list2, 'a', 'e'))
