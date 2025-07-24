#Brute Force
class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        tmp = []
        for num in nums:
            if num == val:
                continue
            tmp.append(num)
        for i in range(len(tmp)):
            nums[i] = tmp[i]
        return len(tmp)

''' TC =o(n) and SC = o(n)'''

# Two Pointers -I
class Solution:
    def removeElement(self,nums,val):
        k = 0
        for i in range(len(nums)):
            if nums[i]!=val:
                nums[k] = nums[i]
                k+=1
        return k

''' TC = o(n) and Sc = o(1) '''

# Two Pointers - II
class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        i = 0
        n = len(nums)
        while i < n:
            if nums[i] == val:
                n -= 1
                nums[i] = nums[n]
            else:
                i += 1
        return n

''' Tc = o(n) and SC = o(1)'''