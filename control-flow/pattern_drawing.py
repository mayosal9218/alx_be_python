# pattern_drawing.py
# A program to draw a square pattern of asterisks using nested loops

# Prompt the user for the size of the pattern
size = int(input("Enter the size of the pattern: "))

# Initialize row counter
row = 0

# Use a while loop for rows
while row < size:
    # Use a for loop for columns
    for col in range(size):
        print("*", end="")
    print()  # move to the next line after each row
    row += 1
