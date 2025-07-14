nums = [[5,20,3],[7,-10,9],[1,-52,6]]
rows = len(nums)
cols = len(nums[0])
for i in range(0,rows):
    for j in range(0,cols):
        print(nums[i][j], end = " ")
    print() #this will print others in other new line


#upper triangle
row = len(nums)
col = len(nums[0])
for i in range(0,row):
    for j in range(0,col):
        if j>=i:
            print(nums[i][j], end = " ")
        else:
            print("*",end = " ")
    print()

#lower triange
row = len(nums)
col = len(nums[0])
for i in range(0,row):
    for j in range(0,col):
        if j<=i:
            print(nums[i][j], end = " ")
        else:
            print("*",end = " ")
    print()