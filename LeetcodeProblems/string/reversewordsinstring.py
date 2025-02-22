st = 'punam is a very good girl'
s = ''
for char in st.split():
    print(char[::-1])
    
    
st = 'punam is a very good girl'
s = ' '.join([char[::-1] for char in st.split()])
print(s)
