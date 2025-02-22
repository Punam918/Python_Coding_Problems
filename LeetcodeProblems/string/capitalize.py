# Capitalize first and last word of each word in a string

s = 'punam is a very good girl'
d = []
for char in s.split():
    if len(char)> 1:
        d.append(char[0].upper() +char[1:-1] + char[-1].upper())
    else:
        d.append(char.upper())
    
print(' '.join(d))