# Indefinate loop
# Python While Loop is used to execute a block of statements repeatedly 
# until a given condition is satisfied. 
# When the condition becomes false, 
# the line immediately after the loop in the program is executed.

# Syntax of while loop
# while expression: # expression is a condition
#     statement(s)
#
# The while loop evaluates the condition before the block of code is executed.

# The while loop is used when you don't know the number of iterations in advance.



# Example of Indefinate loop
# Example 1: Python while Loop
while True:
    print("Enter 'x' for exit.")
    val = input("Enter any value: ")
    if val == 'x':
        break
    else:
        print("Entered value is:",val)
