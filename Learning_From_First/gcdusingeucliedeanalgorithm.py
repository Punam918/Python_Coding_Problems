'''Euclidean Algorithm For GCD'''
def gcd(a, b):
    while b:
        a, b = b, a % b  
    return a


print(gcd(12, 18))  
print(gcd(100, 25)) 
