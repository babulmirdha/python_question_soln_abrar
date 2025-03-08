### **Problem Statement-1:**  
Create a Python program that continuously prompts the user to enter a value. The program should display the entered value and repeat the process indefinitely. However, if the user enters **'x'**, the program should terminate. This ensures that the loop runs indefinitely until a specific exit condition is met.  

**Constraints:**  
- The program should keep asking for user input.  
- It should display the entered value unless the user enters **'x'**.  
- When **'x'** is entered, the loop should break, and the program should stop execution.  

**Example Interaction:**  
```
Enter 'x' for exit.
Enter any value: hello
Entered value is: hello

Enter 'x' for exit.
Enter any value: 123
Entered value is: 123

Enter 'x' for exit.
Enter any value: x
(Program exits)
```  

This problem demonstrates the concept of **indefinite loops** (`while True`) and **conditional termination** (`break`).


### **Problem Statement-2:**  
Develop a Python program that continuously prompts the user to enter a value. The loop should keep running until the user enters **'0'**, at which point the program should terminate. Each entered value (except '0') should be displayed to the user before prompting for the next input.  

**Constraints:**  
- The loop should start with a non-zero condition (`x = 1`).  
- The program should display the entered value unless the user enters **'0'**.  
- When **'0'** is entered, the loop should stop by updating `x = 0`, causing the condition `x != 0` to become `False`.  

**Example Interaction:**  
```
Enter '0' for exit.
Enter any value: hello
Entered value is: hello

Enter '0' for exit.
Enter any value: 42
Entered value is: 42

Enter '0' for exit.
Enter any value: 0
(Program exits)
```

This problem demonstrates the use of an **indefinite loop** (`while x != 0`) and how to control loop termination using a variable (`x`).