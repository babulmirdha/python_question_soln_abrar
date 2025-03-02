# Q13. Write a Python program that creates a new list containing only the positive numbers from a given list.
# Example: Given the list [-1, 2, -3, 4, 5, -6], the program should output [2, 4, 5]


numbers = [-1, 2, -3, 4, 5, -6]

positive_numbers = []

for number in numbers:
    if number > 0:
        positive_numbers.append(number)


print(positive_numbers)
