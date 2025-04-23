def printnamentimes(name,n):
    if n == 0:
        return 
    print(name)
    printnamentimes(name,n-1)
    
print(printnamentimes(('punam'),6))