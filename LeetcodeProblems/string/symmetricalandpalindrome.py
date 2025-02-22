def palindrome(s):
    return s == s[::-1]

def is_symmetrical(s):
    length = len(s)
    mid = length // 2
    if length % 2 == 0:
        return s[:mid] == s[mid:]
    else:
        return s[:mid] == s[mid+1:]

s = "amaama"
if is_symmetrical(s):
    print("Symmetrical")
else:
    print("Not Symmetrical")

if palindrome(s):
    print("Palindrome")
else:
    print("Not Palindrome")
