# Q22. Write a Python program with a list consisting of both positive and negative numbers.
# Ensure that the smallest number is found correctly

numbers = [12, -5, 23, -42, 8, 0, 17, -10]

smallest = numbers[0]


i=1

while i < len(numbers):
    if(numbers[i] < smallest):
        smallest = numbers[i]
    i += 1
    
print(smallest)