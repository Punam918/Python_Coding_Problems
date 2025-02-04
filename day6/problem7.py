'''
Write a Python program to create a list by concatenating a given list with a range from 1 to n.
eg: [q,p] -> [q1,q2,q3,p1,p2,p3]
'''
def concatenate_in_given_range(lst,n):
    result = []
    for item in lst:
        for i in range(1,n+1):
            result.append(f"{item}{i}")
    return result   
initial_list = ['q','p']
n = 3
result = concatenate_in_given_range(initial_list,n)
print(result)

def concatenate(lst,n):
    result = []
    for item in lst:
        for i in range(1,n+1):
            result.append(f"{item}{i}")
    return result
lst = ['q','p']
print(concatenate(lst,n=5))