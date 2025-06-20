nums = [3,1,2,4,5,2,6,4] # important sorting algorithm 


def merge_array(left,right):
    result = []
    i,j = 0,0
    n,m = len(left),len(right)
    while i<n  and j<m:
        if left[i]<=right[j]:
            result.append(left[i])
            i+=1
        else:
            result.append(right[j])
            j+=1
    #after one either left or right kunae exhaust vayo vni we need to add remaining so
    if i<n:
        while i<n:
            result.append(left[i])
            i+=1
    if j<m:
        while j<m:
            result.append(right[j])
            j+=1
    return result


def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])
    return merge_array(left_half, right_half)

sorted_nums = merge_sort(nums)
print("Sorted array:", sorted_nums)

'''
https://www.youtube.com/watch?v=ZDCoxXeksWM&list=PLhR2IpV1b2FwWwviBHRrR118YAaSlyhTU&index=22

TC for second merge_sort =o(log2(n)) if half half vo vni merge ma half half gari raxam
TC  for merge_array = 0(n+m) hunca while loop lagae rako cum 
So, Total TC = o(log2n*n) = o(log2n**2) = o(2log2n)
SC = o(n)

'''