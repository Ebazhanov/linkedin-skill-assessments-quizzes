#!/usr/bin/env python3
"""
This script demonstrates zipping three lists into a list of tuples.

Corresponding to Q28 from the Python quiz: Given three lists of fruits,
quantities, and prices, create a new list that pairs them as tuples.
"""

# Define the lists as given in the quiz
fruits = ['Apples', 'Oranges', 'Bananas']  # List of fruit names
quantities = [5, 3, 4]  # Corresponding quantities for each fruit
prices = [1.50, 2.25, 0.89]  # Corresponding prices for each fruit

# Using zip to combine the three lists into tuples
# zip() pairs elements from each iterable at the same index
groceries = list(zip(fruits, quantities, prices))

# Print the resulting list of tuples
print(groceries)
# Expected Output: [('Apples', 5, 1.5), ('Oranges', 3, 2.25), ('Bananas', 4, 0.89)]
