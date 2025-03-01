#Q9. Write a Python program that finds the largest number in a given list

#Example: Given the list [10, 20, 4, 45, 99, 25, 105, 725, 268,168], the program should output

numbers = [10, 20, 4, 45, 99, 25, 105, 725, 268,168, 159, 753, 1025, 8264, 12, 45, 86]

max_number = 0
for number in numbers:
    if max_number<number:
       max_number = number


print(max_number)




