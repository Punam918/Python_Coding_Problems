'''Print ! to n without using loop'''
def recursion(num):
    if num>0:
        recursion(num-1)
        print(num,end = " ")
        
recursion(8)

'''It follows backtracking to print numbers in ascending order'''