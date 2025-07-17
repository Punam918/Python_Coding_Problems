# using sorting
class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        nums.sort()
        for i in range(1,len(nums)):
            if nums[i] == nums[i-1]:
                return True 
        return False 

#TC  = o(nlogn) Here, Sorting takes nlog(n) and SC = o(n)

#using set 

class solution:
    def containsDuplicat(self, nums:List[int]) -> bool:
        num_set = set()
        for n in nums:
            if n in num_set:
                return true
            num_set.add(n)
        return False
        num_set.add(n)

# Tc = o(n) and sc = o(n)

#checking Length
class solution:
    def containsDuplciate(self, nums:List[int])->bool:
        return True if len(set(nums)) <len(nums) else False

# Tc  = o(n) and SC = o(n)
    