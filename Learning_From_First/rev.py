a= [10, 20, 30, 40, 50]
rev = []
for i in range(len(a)):
    rev = [a[i]] + rev
print(rev)
    