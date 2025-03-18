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

