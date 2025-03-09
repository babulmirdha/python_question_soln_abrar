# Q20. Write a Python program using a while loop to find the smallest number in a list. 
# Example: Given the list [10, 20, 4, 45, 99], the program should output 4

numbers = [10, 20, 4, 45, 99]

smallest = numbers[0]


i=1

while i < len(numbers):
    if(numbers[i] < smallest):
        smallest = numbers[i]
    i += 1
    
print(smallest)