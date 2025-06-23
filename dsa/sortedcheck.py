nums = [3,5,6,8,9,10,20]
#checking if array is sorted or not
def sortedcheck(nums):
    n = len(nums)
    for i in range(0,n-1):
        if nums[i]>nums[i+1]:
            return False
    return True
'''
    TC = o(n) one for loop o(n) other all comparison inside o(1)
    SC = o(1)
'''    