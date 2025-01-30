""" 
Create a custom iterable class that generates a sequence of prime numbers. The class should 
implement both the __iter__ and __next__ methods.
"""
class PrimeNumbers:
    def __init__(self, limit):
        self.limit = limit  
        self.count = 0 
        self.current = 2  

    def __iter__(self):
        return self  

    def __next__(self):
        while self.count < self.limit:
            if self.is_prime(self.current):
                self.count += 1
                prime = self.current
                self.current += 1
                return prime
            self.current += 1
        raise StopIteration  

    def is_prime(self,n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True


N = int(input("Enter the number of prime numbers to generate: "))
prime_iter = PrimeNumbers(N)

for prime in prime_iter:
    print(prime, end=" ")
