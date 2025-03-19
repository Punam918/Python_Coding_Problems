'''Print Name N times Using Recursion'''
def recurname(str,n):
    if n>0:
        recurname(str,n-1)
        print(str)
recurname('punam',8)


def printGfg(n):
    if n > 0:
        print("GFG", end=" ") 
        printGfg(n - 1)  