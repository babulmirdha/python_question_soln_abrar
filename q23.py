# Q23. Write a Python program that counts how many times a specific element (given by the user) occurs in a list using a while loop.

numbers = [2, 5, 3, 7, 5, 8, 5, 1, 9, 5, 4, 5, 6, 5, 0, 5, 5, 5, 5, 5,3,3]

target = int(input("Enter a number: "))
i = 0
count = 0

while i < len(numbers): 
    if numbers[i]==target: 
        count +=1 
    i +=1 

print(f"{target} occurs {count} times in the list")
