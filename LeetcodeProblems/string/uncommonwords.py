# Input : A = “Geeks for Geeks”,  B = “Learning from Geeks for Geeks”
# Output : [‘Learning’, ‘from’]


# Input : A = “apple banana mango” , B = “banana fruits mango”
# Output : [‘apple’, ‘fruits’]

def check(str1,str2):
    s = str1.split()
    d = str2.split()
    e = []
    for char in s:
        if char not in d:
            e.append(char)
    for char in d:
        if char not in s:
            e.append(char) 
    return e       
    
    
    
    
print(check("Geeks for Geeks","Learning from Geeks for Geeks"))
print(check("apple banana mango","banana fruits mango"))