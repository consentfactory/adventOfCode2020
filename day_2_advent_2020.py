# Advent of Code - Day 2
# day_2_advent_2020.py
# 2020.12.02
# Jimmy Taylor

# Reading data from text file, spliting each value as separate lines without line break
input_data = open('inputs/day2.txt').read().splitlines()
# Cleaning up the data in each row to make it easier to parse later as individual rows
modified_data = [line.replace('-',' ').replace(':','').replace(' ',',') for line in input_data]

# Tracking good and bad passwords
valid_passwords_part_1 = 0
bad_passwords_part_1 = 0
valid_passwords_part_2 = 0
bad_passwords_part_2 = 0

for row in modified_data:
    
    row = list(row.split(','))


    # Part 1
    min_val = int(row[0])
    max_val = int(row[1])
    letter = row[2]
    password = row[3]

    # Counting instances of the letter in the password
    letter_count = password.count(letter)

    # Checking if letter count is within the range
    if (letter_count >= min_val) and (letter_count <= max_val):
        valid_passwords_part_1 += 1
    else:
        bad_passwords_part_1 +=1


    # Part 2

    # Subtracting by 1 to calibrate character position
    first_pos = int(row[0]) - 1
    second_pos = int(row[1]) - 1
    letter = row[2]
    password = row[3]
    
    # Looking through the characters and capturing their positions
    positions = [pos for pos, char in enumerate(password) if char == letter]

    # Looking if letter is in both positions; if so, bad password
    if (first_pos in positions) and (second_pos in positions):
        bad_passwords_part_2 +=1
    # If letter in one position, valid password
    elif (first_pos in positions):
        valid_passwords_part_2 += 1
    elif (second_pos in positions):
        valid_passwords_part_2 += 1
    # If letter is not in any position, bad password
    else:
        bad_passwords_part_2 +=1


    
print(f"Part 1 Valid Passwords: {valid_passwords_part_1}")
print(f"Part 1 Bad Passwords: {bad_passwords_part_1}")
print(f"Part 2 Valid Passwords: {valid_passwords_part_2}")
print(f"Part 2 Bad Passwords: {bad_passwords_part_2}")