# Input: arr[] = [1, 2, 3, 4, 5, 6, 7, 8, 9], K = 3 
# Output: 3, 2, 1, 6, 5, 4, 9, 8, 7

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
newarr = []
k = 3

for i in range(0,len(arr),k):    
    print(f"Processing subarray: {arr[i:i+k]}")
    newarr +=reversed(arr[i:i+k])
    
print(newarr)