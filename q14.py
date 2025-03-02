# Q14. Write a Python program that concatenates all the strings in a given list into a single string.
# Example: Given the list ["hello", "world", "python"], the program should output

words = ["hello", "world", "python"]

sentence = ""

for word in words:
    sentence = sentence + word

print(sentence)