'''Print 1 to n without using loop'''
def recursion(num):
    if num>0:
        recursion(num-1)
        print(num,end = " ")
        
recursion(8)
# print(recursion(8))        This will return None because there is no return statement in the function
'''It follows backtracking to print numbers in ascending order'''