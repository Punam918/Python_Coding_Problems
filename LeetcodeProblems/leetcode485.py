nums = [ 1,1,0,1,0,1,1,1,1,0,1,1]
def maxcount(nums):
    count = 0
    max_count = 0 
    for i in range(0,len(nums)):
        if nums[i]==0:
            count+=1
        else:
            max_count = max(max_count,count)
        count = 0
    return max(max_count,count)

''' TC = o(n) If else is o(1) and for loop is o(n) and SC = 0(1)'''