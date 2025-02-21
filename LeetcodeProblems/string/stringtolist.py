# Convert string to a list in Python
p = 'punam'
l=[]
for char in p:
    l.append(char)
    
print(l)

c= 'punam adhikari'
d = []
for char in c.split():
    d.append(char)
    
print(d)


f = list(c)
print(f)