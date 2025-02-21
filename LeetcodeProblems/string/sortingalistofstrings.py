# How to sort a list of strings in Python
lst = ['s','f','d','l','u','e','w']
lstt=[]
for char in sorted(lst):
    lstt+=char
print(lstt)

# Using last character
a = ["banana", "apple", "cherry"]
# Sorting by last character
res = sorted(a, key=lambda s: s[-1])
print(res)

# Sorting by length
res = sorted(a, key=len)
print(res)

# Sorting in reverse order
res = sorted(a, reverse=True)
print(res)