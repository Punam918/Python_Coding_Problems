''' Remove Duplicats from sorted array inplace inside the same array'''
#brute force
nums = [1,1,1,2,3,4,4,7,9,9,9,10]
# we can use extra space though inplace
n = len(nums)
freq_map = {}  #extra space
for i in range(0,n):
    freq_map[nums[i]]=0

j = 0 
for key in freq_map:
    nums[j] = key
    j+=1
return j


'''
TC = o(2n) = o(n)
SC =o(n)
'''


# Optimal
nums = [1,1,1,2,3,4,4,7,9,9,10]
#now inplace 
n = len(nums)
if n == 1:
    return 1 
i = 0 
j = j+1 
while j<n:
    if nums[j]!= nums[i]:
        i+=1 
        nums[i],nums[j] = nums[j],nums[i]
    j+=1 

''' SC = o(1)
    TC = o(n)
'''