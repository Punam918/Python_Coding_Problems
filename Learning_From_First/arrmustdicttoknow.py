arr = [1,2,1,3,2,5]
punu ={}
for i in range(len(arr)):
    punu[arr[i]] = punu.get(arr[i],0) +1
print(punu)
    
    