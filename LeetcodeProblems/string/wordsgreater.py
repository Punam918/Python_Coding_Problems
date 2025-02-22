# Find words which are greater than given length k
# Input : str = "hello geeks for geeks 
#           is computer science portal" 
#         k = 4
# Output : hello geeks geeks computer 
#          science portal
# Explanation : The output is list of all 
# words that are of length more than k.

str = "hello geeks for geeks is computer science portal" 
k = 4
output= []
for char in str.split():
    if len(char)> k:
        output.append(char)
        
print(output)