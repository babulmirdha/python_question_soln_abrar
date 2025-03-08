     
# Example 2: Python while Loop   
x = 1  # Initialize x to a non-zero value to start the loop
while x != 0:
    print("Enter '0' for exit.")
    val = input("Enter any value: ")
    if val == '0':
        x = 0
    else:
        print("Entered value is:", val)