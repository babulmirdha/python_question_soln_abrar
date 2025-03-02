# Q18. Write a Python program using a while loop to count how many times a specific number
# appears in a list. 

# Example: Given the list [1, 2, 3, 4, 2, 2, 5] and the number 2, the program should output 3

# Define the list
numbers = [1, 2, 3, 4, 2, 2, 5]

# Define the number to count
specific_number = 2

# Initialize count and index variables
count = 0

# Initialize index variable
i = 0

while i< len(numbers):
    if numbers[i] == specific_number:
        count += 1
    i += 1
    
    
print("The number", specific_number, "appears", count, "times in the list")