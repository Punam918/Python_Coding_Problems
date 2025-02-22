# Adding one to number represented as array of digits
'''
Input : [1, 2, 4]
Output : 125
Explanation: 124 + 1 = 125 

'''
def add_one(arr):
    num = int(''.join(map(str, arr)))  # Converting list to an integer
    num += 1  
    return num  
inp = [1, 2, 4]
print(add_one(inp))
