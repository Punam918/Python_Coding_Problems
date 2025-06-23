nums = [55,32,-97,99,3,67]
large = float('-inf')
n = len(nums)
for i in range(n):
    large = max(large,nums[i])
return large

'''
    TC = o(N)
    sc = o(1)
'''