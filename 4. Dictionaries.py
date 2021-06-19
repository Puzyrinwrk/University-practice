# Task_1
# Write a function that creates swapped dictionary (keys and values interchanged) for given dictionary.
# In original dictionary multiple keys may refer to the same value, so, new value should be tuple with all corresponding keys.
# Example: dictionary {1:2, 3:4, 5:4, 7:2, 9:4} swapped to {2: (1, 7), 4: (3, 9, 5)}
# Hint: use 'for' loop like in book's section 7.3
# Function signature: def swap_dict(d)

# Task_2
# Write a function that creates compact version of dictionary.
# In compact dictionary keys are grouped by original dict's values into tuples.
# Example: dictionary {1:2, 3:4, 5:4, 7:2, 9:4} compacted to {(3, 9, 5): 4, (1, 7): 2}
# Hint: use 'for' loop like in book's section 7.3
# Function signature: def compact_dict(d)

# Task_1
d1 = {1: 2, 3: 4, 5: 4, 7: 2, 9: 4}


def swap_dict(d):
    rd = {}
    for k, v in d.items():
        rd[v] = rd.get(v, ()) + (k,)
    return rd


print(swap_dict(d1))


# Task_2
def compact_dict(d):
    r = swap_dict(d)
    return {tuple(value): key for key, value in r.items()}


print(compact_dict(d1))
