'''Problem: Find the Most Frequent Element in a List
Write a Python function called most_frequent_element that takes a list of integers as input and 
returns the most frequently occurring element in the list. If there
is a tie (multiple elements with the same highest frequency), return the smallest element among them.'''
def most_frequent_elements(n):
    if not n:
        return None
    frequency = {}
    for num in n:
        frequency[num] = frequency.get(num, 0) + 1
    max_freq = max(frequency.values())
    most_frequent = [key for key,value in frequency.items() if value == max_freq]
    return(most_frequent)
    
nums  = [1,2,3,2,2,3,4,5,6,4,2,1,1,1,3]
print(most_frequent_elements(nums))