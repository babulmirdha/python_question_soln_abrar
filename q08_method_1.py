# Write a Python program that calculates the sum of all elements in a given list.
# Example: Given the list [1, 2, 3, 4, 5], the program should output 15


numbers = [1, 2, 3, 4, 5]
# 1 + 2 = 3
# 3 + 3 = 6
# 6 + 4 = 10
# 10 +5 = 10


# 1st method
sum = 0
for number in numbers:
    sum = sum + number
    print(number)

print(sum)



