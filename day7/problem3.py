''' Avoid Spaces in string length'''
s = 'punam is a good girl'
for char in s.split():
        print(char, end ="")
        
lengt = len([char for char in s if char!=" "])
print(lengt)


