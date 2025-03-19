def reverse_array(arr, start, end):
    if start >= end:
        return

    arr[start], arr[end] = arr[end], arr[start]    
    reverse_array(arr, start + 1, end - 1)

arr = [1, 2, 3, 4, 5] 
reverse_array(arr, 0, len(arr) - 1)
print("Reversed array:", arr)



def printArray(arr, n):
    print("The reversed array is:- ")
    for i in range(n):
        print(arr[i], end=" ")
    print()


def reverseArray(arr, n):
    ans = [0] * n
    for i in range(n - 1, -1, -1):
        ans[n - i - 1] = arr[i]
    printArray(ans, n)

if __name__ == "__main__":
    arr = [5, 4, 3, 2, 1]
    n = len(arr)
    reverseArray(arr, n)