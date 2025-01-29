def prime_check(n):
    if n<=1:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%2 ==0:
            return False
    return True
    
n = int(input("enter a number"))
print('prime_check',prime_check(n))