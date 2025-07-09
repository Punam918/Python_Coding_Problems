'''Rearrange Elements By Sign first positive first negative second positive second negative and so on'''
nums = [5,10,-3,-1,-10,6]
#result should be res = [5,-3,10,-1,6,-10]
#brute force
pos = [5,10,6]
neg = [-3,-1,-10]
def posneg(nums):
    for i in range(0,pos(nums)):
        nums[2*i] = pos[i]
        nums[(2*i)+1] = neg[i]
    return nums

''' TC = o(n +n/2) sc = o(n/2 + n/2)= o(n) '''

#optimal
def rearrange(nums):
    n = len(nums)
    result = [0]*n
    posIndex, negIndex = 0,1
    for i in range(0,n):
        if nums[i]>0:
            result[posIndex] = nums[i]
            posIndex+=2
        else:
            result[negIndex] = nums[i]
            regIndex += 2
    return result
