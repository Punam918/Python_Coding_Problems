'''Palindrome for numbers'''

def checkpalindrome(num):
    original = num
    res = 0
    while num>0:
        last = num%10
        res = res*10+last
        num = num//10
    if original == res:
        return True
    else:
        return False

print(checkpalindrome(121))


def is_palindrome(s):
    s = s.replace(" ", "").lower()
    left = 0
    right = len(s) - 1

    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1

    return True

print(is_palindrome("madam"))        # True
print(is_palindrome("Race car"))     # True
print(is_palindrome("hello"))        # False
