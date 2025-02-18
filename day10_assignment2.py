#Write a Python program to get the largest and smallest number from a list without built in functions.
# Define a list of numbers
numbers = [4, 7, 1, 9, 3, 5]

# Initialize variables to store the largest and smallest values
largest = numbers[0]
smallest = numbers[0]

# Iterate through the list to find the largest and smallest numbers
for num in numbers:
    if num > largest:
        largest = num  # Update largest if current number is larger
    if num < smallest:
        smallest = num  # Update smallest if current number is smaller

# Print the result
print("The largest number in the list is:", largest)
print("The smallest number in the list is:", smallest)

'''output
The largest number in the list is: 9
The smallest number in the list is: 1'''

