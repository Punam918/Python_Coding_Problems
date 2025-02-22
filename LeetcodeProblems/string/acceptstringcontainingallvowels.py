s = "Geeksforgeeksaiou"
v = 'aeiou'

# Check if all vowels are present in the string
if all(i in s.lower() for i in v):
    print("True")
else:
    print("False")
