'''Capitalize the first and last character of each word in a string'''
a = 'punam'
print(a[0].upper()+a[1:4]+a[-1].upper())


def capitalizefirstandlast(strr):
    word = strr.split()
    newstrr = []
    
    for char in word:
        if len(char)==1:
            wor = char.upper()
        else:
            wor = char[0].upper() + char[1:-1] + char[-1].upper()
        newstrr.append(wor)
            
    return " ".join(newstrr)
    
s = "punam is a very good girl"
result = capitalizefirstandlast(s)
print(result)
