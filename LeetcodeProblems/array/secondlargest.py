# Input: arr[] = [12, 35, 1, 10, 34, 1]
# Output: 34

def second_largest(arr):
    first = second = float('-inf') # for smallest no find garda 'inf'
    
    for num in arr:
        if num > first:
            second = first
            first = num
        elif num > second and num != first:
            second = num
    
    return second

arr = [3, 1, 4, 1, 5, 9, 2, 6, 5]
second_max = second_largest(arr)
print("Second Largest Element:", second_max)


arr = [12, 35, 1, 10, 34, 1]
array2 = sorted(arr)

print(array2[-2])
