nums = [1,0,2,4,3,0,0,3,5,1]
n = len(nums)
temp = []
for i in range(0,n):
    if nums[i]!=0:
        temp.append(nums[i]) # o(n)
        

n2 = len(temp)
for i in range(0,n2):  #o(n) for both for loop for 10 to 13
    nums[i] = temp[i]
for i in range(n2,n):  
    nums[i] = 0



''' So, TC = o(n+n) = o(n)'''


#optimal approach with no extra space for temp inplace
nums = [1,0,2,4,3,0,0,3,5,1]
if len(nums) == 1:
    return
i = 0 
while i <len(nums):
    if nums[i] == 0:
        break 
    i+=1 
if i == len(nums):
    return 
j = i+1
    

''' Tc = o(n) , sc = o(1)'''