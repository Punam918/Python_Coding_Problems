#print N to 1 using recursion
def printing(num):
    if num ==0:
        return 
    print(num)
    printing(num-1)
    
print(printing(6))
        
        
#print 1 to N using recursion
def printing(num):
    if num ==0:
        return
    
    printing(num-1)
    print(num)    
    
print(printing(6))
