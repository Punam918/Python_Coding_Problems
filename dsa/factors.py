#factors generation 


#brute force solution 

n = 20 

result = []
for i in range(1,n+1):
    if n%i == 0:
        result.append(i)
# return result  if function 
'''
    TC = o(n)
    sc = o(k) k would be the total number of factors it takes space for result and input
'''
#better approach 
    
result = []
for i in range(1, n//2):
    if n % i ==0:
        result.append(i)
result.append(n)

''' for 10 , 1 2 4 5 10 not 6 7 8 9 because only smaller number can be factors 
     TC = o(n/2) = o(n *1/2) = o(n)
     sc = o(k) k is the amount of factors
'''

no = 36 
'''
     1 - 36 
     2 - 18 
     3 - 12
     4 - 9
     6 - 6
'''
import math
from math import sqrt
result = []
for i in range(1, int(sqrt(no))+1): # for i in range 7 for only 6 because at 6 it stops and we can find its multiplier which is also factor directly.
    if no%i ==0:
        result.append(i)
        
    if no//i != i: # for not appending 6 two times 6*6
        result.append(no//i)
        
result.sort()
        
        
'''
    sorting TC = o(n) + o(nlogn) here o(nlogn) is TC for sorting 
    sc = o(k)
'''