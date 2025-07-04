# Right Rotate array by 1 place
nums = [5,-2,3,9,0,6,10,7]
n = len(nums)
nums  = nums[-1] + nums[0:n-1]

nums = nums[n-1] + nums[0:n-1]

''' TC = o(1)+o(n-1) = 1+ n-1 = n'''

# next method
temp = nums[n-1]
for i in range(n-2,-1,-1):
    nums[i+1] = nums[i]
nums[0] = temp

''' TC = o(n-1), SC = o(1)'''