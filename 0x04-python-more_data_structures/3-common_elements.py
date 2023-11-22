#!/usr/bin/python3

def common_elements(set_1, set_2):
    # Initialize an empty set to store common elements
    common_set = set()

    # Iterate through elements in set_1
    for element in set_1:
        # Check if the element is also in set_2
        if element in set_2:
            # Add the common element to the common_set
            common_set.add(element)

    return common_set

# Example usage:
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

result = common_elements(set1, set2)
print(result)

