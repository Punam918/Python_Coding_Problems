def sortedlist(list1,list2):
    return sorted(list(set(list1+list2)))   
list1 = list(map(int, input("Enter first sorted list: ").split()))
list2 = list(map(int, input("Enter second sorted list: ").split()))
print("Merged sorted list:", sortedlist(list1, list2))
