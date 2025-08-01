#brute force
class Solution:
    def sortColors(self,nums:List[int]) -> None:
        nums.sort()



    '''TC = o(nlogn) and SC = o(1) or o(n)'''

#Counting Sort
class Solution:
    def sortColors(self,nums:List[int]) -> None:
        count = [0]*3
        for num in nums:
            count[num]+=1

        index = 0
        for i in range(3):
            while count[i]:
                count[i]-=1
                nums[index] = i
                index+=1
'''This is inplace sorting method'''
'''TC = o(n) and sc = o(1)'''

#Three Pointers -I
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l, r = 0, len(nums) - 1
        i = 0

        def swap(i, j):
            temp = nums[i]
            nums[i] = nums[j]
            nums[j] = temp
        
        while i <= r:
            if nums[i] == 0:
                swap(l, i)
                l += 1
            elif nums[i] == 2:
                swap(i, r)
                r -= 1
                i -= 1
            i += 1
''' Tc = o(n) and SC =o(1)'''

#Three Pointers -2
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zero = one = two = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                nums[two] = 2
                nums[one] = 1
                nums[zero] = 0
                two += 1
                one += 1
                zero += 1
            elif nums[i] == 1:
                nums[two] = 2
                nums[one] = 1
                two += 1
                one += 1
            else:
                nums[two] = 2
                two += 1
''' Tc = o(n) and sc =o(1)'''

# Three Pointers - III
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zero = one = 0
        for two in range(len(nums)):
            tmp = nums[two]
            nums[two] = 2
            if tmp < 2:
                nums[one] = 1
                one += 1
            if tmp < 1:
                nums[zero] = 0
                zero += 1

'''Tc = o(n) and SC = o(1)'''