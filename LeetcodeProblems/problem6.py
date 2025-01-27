''' Eliminating duplicates from the sequence preserving the order of the items. '''
def remove_duplicates(sequence):
    result = []
    for item in sequence:
        if item not in result:
            result.append(item)
    return result

 
sequence = [1,2,3,4,2,1,3,4,5,6,6,78,3,3]
print(remove_duplicates(sequence))


'''Eliminating duplicates from the sequence using set'''
def remove_duplicates(sequence):
    seen = set()
    result = []
    for item in sequence:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result

sequence = [1, 2, 2, 3, 4, 3, 5, 1, 6]
print(remove_duplicates(sequence))
