'''
Prestoring values into some data structure lne 
list/Dictionary/sets and fetching it

'''

#Hashing 
# brute force approach

n = [5,3,4,6,2,7,8,]
nm = [1,2,3,6,4,5]
for num in nm:
    count = 0 
    for x in n:
        if x ==num:
            count+=1
    print(count)
    
'''
TC = O(m*n) two for loop  n length n , nm length m
SC = o(1)  only count variable 
'''

hash_list = [0]*11
for num in n:
    hash_list[num]+=1
    
    
for num in nm:
    if num<1 or num>10:
        print(0)
    else:
        print(hash_list[num])
        
        
    """
    Tc  = o(n+m) = 10^8 + 10^8 = 2*10^8 so there will be no TLE
    SC =o(11) --> SC = 0(1) constant so i write o(1)
    """
    
