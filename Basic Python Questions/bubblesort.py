def bubble_sort(arr):
    coun = len(arr)
    for i in range(coun):
        for j in range(coun-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
    return arr
num = list(map(int,input("enter a number but seperate it with spaces:").split()))
print(bubble_sort(num))