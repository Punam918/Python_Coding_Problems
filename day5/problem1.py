'''write a Python program that takes user input and appends it to a text file. Also write a program that 
overwrites the existing content of a file with new data.'''

# opening file in append mode to append
with open("example.txt", "a") as file:
    user_input = input("Enter text to append: ")  
    file.write(user_input + "\n") 
print("Your input has been appended to 'example.txt'.")

# Opening file in write mode ('w') for overwritting
with open("example.txt", "w") as file:
    new_content = input("Enter new content (this will overwrite the file): ") 
    file.write(new_content + "\n")

print("The file 'example.txt' has been overwritten with your new content.")
