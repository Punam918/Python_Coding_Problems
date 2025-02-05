'''Count number of vowels using sets in given string'''

s = 'punam is a very good girl'
vowels = {'a','e','i','o','u'}
d = []
count = 0

for char in s:
    if char in vowels:
        d.append(char)
        count+=1
        
print(d)

print(count)