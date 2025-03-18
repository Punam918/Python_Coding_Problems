def checkprime(num):
    if num <= 1:
        return False
    for i in range(2,num):
        if num%i ==0:
            return False
    return True
print(checkprime(17))


'''But This approach below reduces time complexity'''
import math

def checkprime(num):
    if num <= 1:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):  
        if num % i == 0:
            return False
    return True

print(checkprime(17)) 
print(checkprime(18))  
