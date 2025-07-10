#Longest Consecutive Sequence 
#brute force
nums = [1,99,101,98,2,5,3,100,1,1]
max_count = 0
def consecutivesequence(nums):
    n = len(nums) 
    for i in range(0,n): #o(n)
        num = nums[i]
        count =1 
        while num+1 in nums: #o(n)
            count+=1
            num = num +1 
            max_count = max(max_count,count)
    return max_count

''' TC = 0(n**2)  sc = 0(1)'''
