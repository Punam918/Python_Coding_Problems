def fibo_series(n):
    a,b = 0,1
    result = []
    for _ in range(n):
        result.append(a)
        a,b = b,a+b
    return result
num = int(input("enter a number"))
print('fibo_series:',fibo_series(num))