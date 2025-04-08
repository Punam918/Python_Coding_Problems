def fibo_series(n):
    a,b = 0,1
    result = []
    for _ in range(n):
        result.append(a)
        a,b = b,a+b
    return result
num = int(input("enter a number"))
print('fibo_series:',fibo_series(num))



prev2 = 0
prev1 = 1
print(prev2)
print(prev1)

for fibo in range(18):
    newfibo = prev2 + prev1
    print(newfibo)
    prev2 = prev1
    prev1 = newfibo