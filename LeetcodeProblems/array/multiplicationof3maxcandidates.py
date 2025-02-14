# Input:  arr[ ] = [10, 3, 5, 6, 20]
# Output: 1200
# Explanation: Multiplication of 10, 6 and 20

arr = [10, 3, 5, 6, 20]
data = sorted(arr)
print(data[-1]*data[-2]*data[-3])
    # print(i[-1]*i[-2]*i[-3])