'''Recursive way of calculation sum 1.functional way 2. parameterized way'''
#parameterized way
def func(n, total_sum):

    if n < 1:
        print(total_sum)
        return
    func(n - 1, total_sum + n)
n = 3
func(n, 0)

#functional way
def func(n):

    if n == 0:
        return 0

    return n + func(n - 1)
n = 3
print(func(n))
