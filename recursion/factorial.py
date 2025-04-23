def factori(n):
    if n == 0:
        return 1
    else:
        return n * factori(n-1)
print(factori(6))