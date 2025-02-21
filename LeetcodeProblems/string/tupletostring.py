# To convert tuple to string
t = (1, 2, 3, 'Learn', 'Python', 'Programming')
res = '' #This is a string
for val in t:
    res+=str(val)+' '
    
print(res)
print(type(res))