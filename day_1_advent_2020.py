# Advent of Code - Day 1
# day_1_advent_2020.py
# 2020.12.02
# Jimmy Taylor

# Reading data from text file, spliting each value as separate lines without line break
input_data = open('inputs/day1.txt').read().splitlines()
# Converting each value in the input_data list from string to integer
input_data = list(map(int,input_data))

# Creating exit signal when value is found
exit_signal = False
# Looping through first list of integers
for i in input_data:
    # Looping through second set to find two values that sum to 2020
    for x in input_data:
        sum_2020 = i + x
        # If sum found, print values and product of two values, then exit
        if sum_2020 == 2020:
                print(f"Value 1: {i}\nValue 2: {x}")
                print(f"Product of two values: {i*x}")
                exit_signal = True
                break
    if exit_signal:
        break
