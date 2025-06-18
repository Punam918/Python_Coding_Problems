# This is head Recursion
def func(x,n):
    if n == 0:
        return 
    print(x)
    func(x,n-1)
func(15,4) 
# 15 will be printed 4 times 4 then 3 then 2 and then 1 


# print 1 to 5 using recursion 

def func(i,n):
    if i>n:
        return 
    print(i)
    func(i+1,n)
func(1,4)
    
    
# This is a tail recursion also known as BackTracking.
# This is not 1 to n but n to 1 using tail recursion.
def func(i,n):
    if i>n:
        return 
    func(i+1,n)
    print(i)    # TC =O(n) and SC= 0(n) = this is a stack space which involves recursion.