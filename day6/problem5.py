'''
Write a Python program to check if each number is prime in a given list of numbers. Return True if all numbers are prime otherwise False.
Sample Data:
([0, 3, 4, 7, 9]) -> False
([3, 5, 7, 13]) -> True
([1, 5, 3]) -> False
'''

def isprime(seq):
    for item in seq:
            if item < 2:
                return False
            for i in range(2, int(item ** 0.5) + 1):
                if item%i == 0:
                    return False
            return True
        
print(isprime([0,3,4,7,9]))
print(isprime([3,5,7,13]))
print(isprime([1,5,3]))