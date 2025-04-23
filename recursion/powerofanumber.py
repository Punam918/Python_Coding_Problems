#powerofanumberusingrecursion
def powerofnum(a,b):
    if b ==0:
        return 1  # a ko ^0 is 1   
    else:
        return a * powerofnum(a,b-1)    # a* a^(b-1)
    
print(powerofnum(6,7))