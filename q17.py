# Q17. Write a Python program using a while loop to find the sum of all the numbers in a list.
# Example: Given the list [1, 2, 3, 4, 5], the program should output 15


# Define the list
numbers = [1, 2, 3, 4, 5]

# Initialize sum and index variables
total = 0
i = 0

# Iterate through the list using a while loop
while i < len(numbers):
    total += numbers[i]
    i += 1 # Increment the index: i = i + 1

# Print the result
print("Sum of all numbers in the list:", total)
