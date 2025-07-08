''' Maximum SubArray Sum'''


#brute force
nums = [-2, 1 ,-3, 4, -1, 2, 1, -5, 4]
n = len(nums)
total = 0 
maxi = float('-inf')
for i in range(0,n):
    for j in range(1,n):
        total = total + nums[j]
        maxi = max(maxi,total)

return maxi

''' TC = O(n**2)' sc = o(1)'''


#better approach 
#cadains algorithm 
n = len(nums)
maxi = float("-inf")
total = 0 
for i in range(0,n):
    total = toal + nums[i]
    maxi = max(maxi,total)
    if total<0:
        total = 0
return maxi 