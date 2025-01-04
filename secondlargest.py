def second_largest(n):
    arr = list(set(n))
    arr.sort()
    return arr[-2]

num = list(map(int,input("enter a number seperated with spaces").split()))
print(second_largest(num))
