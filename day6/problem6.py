'''
Write a Python program to find the second largest number in a list.

'''

# l = [2,3,4,5,6666,7777,889,999]
# for item in l:
#     if item!=max(l):
#         print(item)
def secondlargest(seq):
    s = sorted(seq)
    return s[-2]        
print(secondlargest([2,3,4,5,6666,7777,889,999]))