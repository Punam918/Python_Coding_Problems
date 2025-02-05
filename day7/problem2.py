
'''Remove i’th character from string'''
def removech(s,i):
    return s[:i]+s[i+1:]
    
s = 'hello'
i = 1
print(removech(s,i))
