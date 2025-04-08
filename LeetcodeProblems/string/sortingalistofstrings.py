# How to sort a list of strings in Python
lst = ['s','f','d','l','u','e','w']
lstt = []
for char in sorted(lst):
    lstt.append(char)
    
print(lstt)

# Using last character
a = ["banana", "apple", "cherry"]
b = sorted(a, key=lambda x: x[-1])  # Sorting based on last character
print(b)

res = sorted(a, key=len)
print(res)

res = sorted(a, reverse=True)
print(res)

res = sorted(a, key=len,reverse = True)
print(res)