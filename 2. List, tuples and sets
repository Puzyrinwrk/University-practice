# Task_1
# Write a simple function which removes three largest elements from integer list (list's size >= 3) and returns result list.
# If largest element is non-unique on some step remove the closest to the end of the list.
# Original list shouldn't be modified.
# Function signature: def remove_3_largest(lst)
# Example: remove_3_largest([1, 2, 3, 1, 2, 3]) should produce [1, 2, 1]

# Task_2
# Write a function which gets 4 lists of numbers and output number of unique ones. For example, if input is
# 1,2,3
# 1,2,3
# 3,4,5
# 3,2,1
# then result has to be 3.
# Function signature: def get_unique_lists_num(a, b, c, d)
# Implementation hint: you can use sets (simpler solution) or 'in' (more advanced solution) operation

# Task_3
# Write a function which gets two lists of positive integers and outputs the largest common integer or zero if common integer not found.
# Function signature: def get_max_common(a,b)


# Task_1
h = [5, 6, 7, 8, 9, 10, 9, 20, 15, 16, 17, 19, 20, 21, 22]

def remove_3_largest(lst):
    b = lst
    b.reverse()
    b.remove(max(lst))
    b.remove(max(lst))
    b.remove(max(lst))
    b.reverse()
    return b

print(remove_3_largest(h))

# Task_2
a1 = [5, 6, 7, 8, 9, 10, 9, 14, 15, 16, 17, 19, 20, 21, 23]
b1 = [5, 6, 7, 8, 9, 10, 9, 14, 15, 16, 17, 19, 20, 21, 23]
c1 = [15, 16, 17, 18, 19, 1, 9, 4, 5, 6, 1, 9, 2, 1, 2]
d1 = [5, 6, 7, 8, 9, 10, 9, 14, 15, 16, 17, 19, 20, 21, 23]


def get_unique_lists_num(a, b, c, d):
    return len(set(map(tuple, (a, b, c, d))))

print(get_unique_lists_num(a1, b1, c1, d1))

# Task_3
x = [6, 4, 4, 5]
y = [0, 0, 2, 5, 3]


def get_max_common(a, b):
    return max(set(a) & set(b) | set([0]))


print(get_max_common(x, y))
