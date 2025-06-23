nums = [4,1,7,6,3,2,8]
'''
    Pick a pivot can be any element first last middle.
    Put pivot at its correct position/index.
    Then place the element less than it at left and greater than it to right.
    Then take pivot for both the sides 
    At left side again do the same and keep small elements at it's left and greater at it's right,
    so same for right side take pivot and sort
'''

def partition (nums,low,high):
    pivot = nums[low]
    i = low, j = high 
    while i<j:
        while nums[i]<=pivot and i<high-1:
            i+=1
        while nums[j]>pivot and j>=low+1:
            j-=1
        if i<j:
            nums[i],nums[j] = nums[j],nums[i]
            
    nums[low],nums[j] = nums[j],nums[low]
    return j    

def quick_sort(nums,low,high):
    if low<high:
        pindex = partition(nums,low,high)
        quick_sort(nums,low,pindex-1)
        quick_sort(nums,pindex+1,high)
        
'''
    TC = o(logn*n)
    TC =o(nlogn)
    SC =o(1)
'''        