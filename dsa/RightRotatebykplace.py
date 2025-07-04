nums = [3,9,5,6,7,2]
n = len(nums)
k = 3 #rotation value
rotations = k%n 
for _ in range(0,rotations): # o(r)

    e = nums.pop() #o(1)
    nums.insert(0,e) #o(n)

print(nums)
''' Tc = o(r*n)'''

n = len(nums)
k = n%k
nums[:] = nums[n-k:] + nums[:n-k]