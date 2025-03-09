# Q24. Create a list with elements 9,8,7,6,5.
# Ask the user whether they need to change any element, if the user enter "Y" - then ask for the
# index and element to be inserted and change the elements in the list accordingly
# Repeat it until the user enters "N" and print the new list


numbers = [9,8,7,6,5]

while True:
    print("\nCurrent List:",numbers)
    
    choice = input("Do you want to change any element? (Y/N): ")
    
    if(choice == 'N'):
        break
    
    if(choice =='Y'):
        index = int(input("Enter the index: "))
        element = int(input("Enter the element: "))
        numbers[index] = element


print("\nNew List:",numbers)