#Write a Python program to find duplicate values from a list and display those.
# Define a list with some duplicate values
numbers = [4, 7, 2, 9, 3, 7, 4, 6, 8, 9]

# Create an empty list to store duplicates
duplicates = []

# Iterate through the list to find duplicates
for num in numbers:
    # If the number appears more than once and is not already in the duplicates list
    if numbers.count(num) > 1 and num not in duplicates:
        duplicates.append(num)

# Print the result
print("Duplicate values in the list are:", duplicates)

'''output
Duplicate values in the list are: [4, 7, 9]'''
