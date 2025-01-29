def remove_duplicates(lst):
    return list(set(lst))
arr = list(map(int,input("Enter a Number:").split()))
print(remove_duplicates(arr))