# Q15. Write a Python program that calculates the product of all numbers in a list
# Example: Given the list [2, 3, 4], the program should output 24

numbers = [2, 3, 4]

product = 1

for number in numbers:
    product = product * number
    
print(product)