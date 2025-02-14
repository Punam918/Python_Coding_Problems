# Input: arr[] = [1, 2, 0, 4, 3, 0, 5, 0]
# Output: arr[] = [1, 2, 4, 3, 5, 0, 0, 0]

arr = [1, 2, 0, 4, 3, 0, 5, 0]
newag = []


for i in arr:    
    if i !=0:
        newag.append(i)
for i in arr:
    if i == 0:
        newag.append(i)
print(newag)


