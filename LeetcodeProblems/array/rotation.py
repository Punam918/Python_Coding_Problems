# Input: arr[] = {1, 2, 3, 4, 5, 6}, d = 2
# Output: {3, 4, 5, 6, 1, 2}
# Explanation: After first left rotation, arr[] becomes {2, 3, 4, 5, 6, 1} and after the second rotation, arr[] 
# becomes {3, 4, 5, 6, 1, 2}

arr = [1, 2, 3, 4, 5, 6]
d = 2
newarr = []
for i in arr:
    