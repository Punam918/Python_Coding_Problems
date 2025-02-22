# Count the Number of matching characters in a pair of string
s1 = "VISHAKSHI"
s2 = "VANSHIKA"
d = []
for char in s1:
    if char in s2:
        d.append(char)
        
print(d)
print(len(d))
        
    
    
    
from collections import Counter
s1 = "VISHAKSHI"
s2 = "VANSHIKA"
# Count characters
c1 = Counter(s1.lower())
c2= Counter(s2.lower())
# Find common characters and sum their counts
res = sum((c1 & c2).values())
print(res)   