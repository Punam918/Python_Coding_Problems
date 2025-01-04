def palindrome_check(n):
    return str(n) == str(n[::-1])
value = input("enter a value")
print("palindrome check:",palindrome_check(value))

