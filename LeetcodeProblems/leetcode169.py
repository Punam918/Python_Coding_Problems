#Brute Force
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        for num in nums:
            count = sum(1 for i in nums if i == num)
            if count > n//2:
                return num 
        
#  ''' TC = o(n**2) and sc = o(1)'''   

#Hash map 
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = defaultdict(int)
        res = maxCount = 0
        for num in nums:
            count[num]+=1
            if maxCount < count[num]:
                res = num 
                maxCount = count[num]
        return res

''' TC = o(n) and SC =o(n) '''

#sorting 
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        return nums[len(nums) // 2]

# TC  = o(nlogn) and sc = o(1) or o(n)


'''Bit Manipulation'''
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        bit = [0] * 32
        for num in nums:
            for i in range(32):
                bit[i] += ((num >> i) & 1)
        
        res = 0
        for i in range(32):
            if bit[i] > (n // 2):
                if i == 31: 
                    res -= (1 << i)
                else:
                    res |= (1 << i)
        return res
''' TC = o(n*32) and sc = o(32) '''

#Boyer-Moore Voting Algorithm
class Solution:
    def majorityElement(self, nums):
        res = count = 0

        for num in nums:
            if count == 0:
                res = num
            count += (1 if num == res else -1)
        return res

'''TC = o(n) and SC = o(1) '''

#Randomization 
class Solution:
    def majorityElement(self, nums):
        n = len(nums)
        while True:
            candidate = random.choice(nums)
            if nums.count(candidate) > n // 2:
                return candidate
''' TC = o(n) and o(1) '''

