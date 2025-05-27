# recurisve sum of a list
def recursivesum(lst):
    if not lst:  #if the list is null return 0
        return 0
    else:
        return lst[0] + recursivesum(lst[1:])
print(recursivesum([3,4,5,6])) 


def recursivesum(lst):
    if not lst:
        return 0
    else:
        return lst[0]+recursivesum(lst[1:])
print(recursivesum([1,2,3,4]))
    