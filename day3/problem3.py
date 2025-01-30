"""
Write a generator function that yields the Fibonacci sequence up to a specified limit.  Then use this 
generator to display the first N Fibonacci numbers.

"""
def fibonacci(limit):
    a, b = 0, 1
    count = 0
    while count < limit:
        yield a
        a, b = b, a + b
        count += 1


N = int(input("Enter the number of Fibonacci numbers to display: "))

fib_gen = fibonacci(N)
for items in fib_gen:
    print(items,end = " ")
