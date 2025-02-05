'''Count the Number of matching characters in a pair of string'''
a = 'punam'
b = 'pugrc'
count = 0
c = []
d = []

for char in a:
    c.append(char)
    
for char in b:
    d.append(char)
    
    
print(c)
print(d)
for i in c:
    for j in d:
        if i==j:
            count+=1
print(count)