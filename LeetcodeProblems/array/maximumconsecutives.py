# Input: arr[] = {1, 1, 0, 0, 1, 0, 1, 0, 1, 1, 1, 1}
# Output: 4
# Explanation: The maximum number of consecutive 1’s in the array is 4 from index 8-11.

arr = [1, 1, 0, 0, 1, 0, 1, 0, 1, 1, 1, 1] 
count = 0
for i in arr:
    if i==1:
        count+=1
    else:
        count =0

print(count)
