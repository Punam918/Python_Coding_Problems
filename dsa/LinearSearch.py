nums = [5,3,9,8,1,6,4,-10,-100]
# implementing Linear Search
n = len(nums)
target = 4 # to see at which index 4 is occuring at nums
for i in range(0,n):
    if nums[i] == target:
        return i 
    
return -1