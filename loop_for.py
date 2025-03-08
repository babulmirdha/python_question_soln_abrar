#two types of loops
# 1. Definite loop
     # a. for in range
     # b. for in list
     # c. for in string
# 2. Indefinite loop
     # a. while loop

# example of definate loop

print("********* range(10) or range(0,10,1) ************")
for i in range(0,10,1): # range( i = 0, i < 10, i = i+1 ) or range(0,10,1)
     print(i)

# example of definate loop with step
print("********* range(0,10,2) ************")
for i in range(0,10,2): # range( i = 0, i < 10, i = i+ 2 )
     print(i)

# example of definate loop with step
print("********* range(1,10,2) ************")
for counter in range(1,10,2):
     print(counter)

# example of definate loop with step by 5
print("********** range(1,100,5) ***********")
for counter in range(1,100,5):
     print(counter)
     
# example of definate loop with step by 5

print("******** range(10,100,10) *************")
for counter in range(10,100,10):
     print(counter)


fruits = ["apple", "banana", "cherry"]

#for range
print("******** range(len(fruits)) *************")
for i in range(len(fruits)):
     print(fruits[i])

#for list
print("******** for in *************")
for x in fruits:
  print(x)
  
#for string
for x in "banana":
  print(x)

  
name = "Abrar"
for x in name:
     print(x)
     
for i in range(0, len(name), 1):
     print(name[i])
     

  




