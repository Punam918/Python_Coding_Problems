s = "Geeksforgeeks"
v = 'aeiou'

if all in (i in s.lower() for i in v):
    print("True")
else:
    print("False")