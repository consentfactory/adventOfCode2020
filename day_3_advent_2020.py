# Advent of Code - Day 3
# day_3_advent_2020.py
# 2020.12.03
# Jimmy Taylor

import math

# Reading data from text file, spliting each value as separate lines without line break
input_data = open('inputs/day3.txt').read().splitlines()

# Part 1

# Tracking tree counts
tree_counter = 0
# Variable using to track right slope movement
position_tracker = 3
# Used for expanding dataset to the right as position_tracker expands
repeat_tracker = 1

# Changing input_data from list to iterator to start on second line
data_iter = iter(input_data)
next(data_iter)

# Looping through data
for row in data_iter:
    # Initiating row so that it has correct width for position_tracker
    row_updated = row * repeat_tracker
    # Getting length of row
    total_col = len(row_updated)

    # If position_tracker value is larger than length of row, expand it as needed
    while position_tracker >= total_col:
        repeat_tracker += 1
        row_updated = row_updated * repeat_tracker
        total_col = len(row_updated)

    # If tree is found, count it
    if row_updated[position_tracker] == '#':
        tree_counter += 1
    
    # Move to the right 3 spaces
    position_tracker += 3

print(tree_counter)


# Part 2

# Tracking each new slope; left is right movement, second is down
slopes = [[1,1],[3,1],[5,1],[7,1],[1,2]]

# List for capturing total trees
trees = []

for slope in slopes:
    
    # Tracking tree counts
    tree_counter = 0
    # Setting right movement from slope list item
    position_tracker = slope[0]
    # Used for expanding dataset to the right as position_tracker expands
    repeat_tracker = 1

    # Changing input_data from list to iterator to start on second line
    data_iter = iter(input_data)
    next(data_iter)

    # Looping through data_iter and skipping lines equal to down slope
    for line, row in enumerate(data_iter, start=1):
        # Looks for modulus of 0, meaning its a line we want to act on
        if line % slope[1] == 0:
            # Initiating row so that it has correct width for position_tracker
            row_updated = row * repeat_tracker
            # Getting length of row
            total_col = len(row_updated)

            # If position_tracker value is larger than length of row, expand it as needed
            while position_tracker >= total_col:
                repeat_tracker += 1
                row_updated = row_updated * repeat_tracker
                total_col = len(row_updated)

            # If tree is found, count it
            if row_updated[position_tracker] == '#':
                tree_counter += 1

            # Move to the right equal to current slope right speed 
            position_tracker += slope[0]

    # Add total trees encountered to trees list
    trees.append(tree_counter)
    print(tree_counter)

print(trees)
# Print the product of each trees value
print(math.prod(trees))