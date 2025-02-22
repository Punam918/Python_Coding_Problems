# Remove All Duplicates from a Given String in Python
s = 'punamisaverygoodgirl'
d = []
for char in s:
    if char not in d:
        d.append(char)
        
print(''.join(d))
