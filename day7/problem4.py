'''print even length words in a string'''

a = 'punam is a very good girll'
for char in a.split():
    if len(char)%2==0:
        print(char,end =" ")
    