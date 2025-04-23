def reversestring(s):
    if len(s)<1:
        return s
    else:
        return reversestring(s[1:])+s[0]
    
print(reversestring('punam'))