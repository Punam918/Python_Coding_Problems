# Python program to print even length words in a string
st= 'hi, how are you?  you are so bea ti ful'
for char in st.split():
    if len(char)%2==0:
        print(char)