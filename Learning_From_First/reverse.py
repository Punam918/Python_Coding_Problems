str_a ='punam'
rev = ''
for char in str_a:
    rev = char+rev    
print(rev)

print(str_a[::-1])

# using index
str_b = 'adhikari'
rev = ''
for i in range(len(str_b)):  #len chae string ma milca but int ma launa mildaina
    rev = str_b[i]+rev
print(rev)

str_c = 'chettri'
rev = ''
for i in range(len(str_c)-1,-1,-1):
    rev = rev + str_c[i]
    
print(rev)