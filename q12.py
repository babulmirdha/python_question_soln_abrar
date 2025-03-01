# Q12. Write a Python program that creates a new list containing the squares of all elements in a given list.
# Example: Given the list [1, 2, 3, 4], the program should output [1, 4, 9, 16]


numbers = [1, 2, 3, 4]
squares = []

for number in numbers:
    squares.append(number**2)

print(squares)