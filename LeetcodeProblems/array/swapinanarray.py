def swap_elements(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]
    return arr

arr = [3, 1, 4, 1, 5, 9, 2, 6, 5]
swapped_arr = swap_elements(arr, 1, 4)
print("Array after swapping:", swapped_arr)
