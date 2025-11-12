#!/usr/bin/env python3
"""
This script demonstrates nested for loops printing combinations of characters and numbers.

Corresponding to Q35 from the Python quiz: What does this function print?
"""

def print_alpha_nums(abc_list, num_list):
    """
    Prints each character from abc_list paired with each number from num_list.

    Args:
        abc_list (list): List of characters (e.g., ['a', 'b', 'c'])
        num_list (list): List of numbers (e.g., [1, 2, 3])
    """
    for char in abc_list:  # Outer loop over characters
        for num in num_list:  # Inner loop over numbers
            print(char, num)  # Print each pair
    return  # Function returns None implicitly

# Call the function with the quiz example
print_alpha_nums(['a', 'b', 'c'], [1, 2, 3])

# Expected Output:
# a 1
# a 2
# a 3
# b 1
# b 2
# b 3
# c 1
# c 2
# c 3
