'''Check if a string has at least one letter and one number'''
a = 'punam062 is4'
print(a.isdigit())
print(a.isalpha())
for char in a:
    print(char)       
def check(strr):
    for char in strr:
        hasalpa = any(char.isalpha() for char in strr)
        hasdigi = any(char.isdigit() for char in strr)
    return hasalpa and hasdigi
print(check('punam062 is44'))