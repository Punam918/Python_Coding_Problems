'''
Doing frequency mapping  can be done through hasing 

'''

nums = [5,6,7,7,9,111,1,1,5,1,1]
freq_map = {}  # not set but empty dictionary can also write dict()
for i in range(0,len(nums)):
    if nums[i] in freq_map:
        freq_map[nums[i]]+=1
    else:
        freq_map[nums[i]] = 1
        
        
print(freq_map)


'''
    TC = 0(n) going through n terms
    SC = 0(n)
'''

hash_map =dict()
n = len(nums)
for i in range(0,n):
    hash_map[nums[i]] = hash_map.get(nums[i],0)+1
    


'''
Iterates over each index i of the list nums.

For each nums[i], it does the following:

hash_map.get(nums[i], 0) retrieves the current count of nums[i] from the dictionary. If it doesn’t exist, it defaults to 0.

It adds 1 to that count.

Then it stores the updated count back in hash_map[nums[i]].
'''

