#Two Sum 
#brute force
def twosum(nums,target):
    n = len(nums)
    for i in range(0,n-1):
        for j in range(i+1,n):
            if nums[i]+nums[j]==target:
                return [i,j]

print(twosum([1,2,3,4,5,6],7))

''' TC = o(n*(n+1)/2 = o(n**2)  SC = o(1)'''
#optimal
nums = [5,9,1,2,4,15,6,3]
def twos(nums,target):
    n = len(nums)
    hash_map = {}
    for i in range(0,n):
        remaining = target - nums[i]
        if remaining in hash_map:
            return [hash_map[remaining],i]
        



''' TC = o(n) if else is o(1) so total = o(n), sc = o(n)'''        