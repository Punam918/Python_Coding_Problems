'''Remove all duplicates from a given string'''

s = 'punam is a very good girl'
d = []

for char in s:
    d.append(char)
    
d =list(set(d))
print("".join(d))
