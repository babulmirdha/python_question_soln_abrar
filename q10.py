# Q10. Write a Python program that counts how many times a specific element appears in a list.

# Example: Given the list [1, 2, 2, 3, 4, 4, 4, 5] and the target number 4, the program should output 3


numbers = [1, 2, 2, 3, 4, 4, 4, 5]

target = 2
count = 0

for number in numbers:
    if number == target:  # if the number is the target number increment the count
        count = count + 1

print(count)