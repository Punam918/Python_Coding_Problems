'''     
    Recursion is very imp, It's concepts extends for dynamic programming also.
    
    def greet():
        print("punam")
    it will not run 
    we need to call 
    
    Function = when a function calls itslef it is called recursion.
    def greet():
        print("punam")
        greet()
    This will call but it will not stop so it is infinite recursion. 
    And it gives Stack Overflow error.
    Though it goes at 987 recursion for then python will throw stack overflow error.
'''

''' print punam for 4 times'''
#head recursion
count = 0 # for determining the cout of no of times the loop is running
def func():
    if count == 4:
        return 
    print("punam")
    count+=1
    func()
    
    """
    Tc = function call o(1), count also same,
    so for TC = o(n+1) n for 4 times can be any times so n 
    so TC = o(n)
    sc = o(n+1) == o(n)
    """
    
# another way 
#tail recursion 
def func():
    if count == 4:
        return 
    count +=1
    func()
    print("punam")
    
    
    """
    Tc = function call o(1), count also same,
    so for TC = o(n+1) n for 4 times can be any times so n 
    so TC = o(n)
    sc = o(n+1) == o(n)
    """