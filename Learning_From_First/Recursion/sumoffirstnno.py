'''Recursive way of calculation sum 1.functional way 2. parameterized way'''
#parameterized way
def func(n, total_sum):
    # Base Condition
    if n < 1:
        print(total_sum)
        return
    
    # Recursive call to decrement i and add to sum
    func(n - 1, total_sum + n)
n = 3
func(n, 0)

#functional way
def func(n):
    # Base Condition
    if n == 0:
        return 0
    
    # Recursive step: sum of n + func(n-1)
    return n + func(n - 1)


n = 3
print(func(n))
