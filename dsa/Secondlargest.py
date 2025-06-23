nums = [55,32,97,-55,45,32,88,21]

# #brute force
nums.sort()
n = len(nums)
return nums[-2]/nums[n-2]
'''
    TC = o(nlogn)
    SC  =o(1)
'''


#better approach
largest = second_largest = float('-inf')
n = len(nums)
for i in range(n):
    largest = max(largest,nums[i])
    
for i in range(n):
    if nums[i]>second_largest and nums[i]!=largest:
        second_largest = nums[i]
return  second_largest

'''
    TC = o(N+N) = 2 times for loop = o(2n) = o(n)
    SC = o(1)
'''

#optimal approach 
largest = s_largest = float('-inf')
n = len(nums)
for i in range(n):
    
    if nums[i]>largest:
        second_largest = largest
        largest = nums[i]
    elif nums[i]>second_largest and nums[i]!=largest:
        s_largest = nums[i]
return s_largest

'''
    TC = o(n) //one big for loop other all o(1) for TC 
    SC = o(1)
'''