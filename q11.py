# Q11. Write a Python program that prints all the even numbers from a given list
# Example:Given the list [1, 2, 3, 4, 5, 6, 7, 8, 9], the program should output 2, 4, 6, 8


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

for number in numbers:
    if number%2 == 0:
        print(number)