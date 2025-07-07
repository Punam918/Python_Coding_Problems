nums = [1,0,3,4]  #missing one is 2
nums = [9,6,4,2,3,5,7,0,1] #missing 8 

#brute force
def findmissing(nums):
    n = len(nums)
    for i in range(0,n+1): #o(n)
        if i not in nums:  #o(n)
            return i 
        
''' TC = o(n**2) sc = o(1)'''


# Better Approach
nums = [1,0,3,4]
def findmissing(nums):
    n = len(nums)
    freq = {}
    for i in range(0,n+1):
        freq[i]=0

    for num in nums:
        freq[num] = 1

    for k,v in freq.items():
        if v == 0:
            return k
        
''' Tc =  o(n) + o(n) + o(n) = o(3n) = o(n)'''
''' SC  = o(n)'''