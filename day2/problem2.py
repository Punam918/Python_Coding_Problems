'''
 2. You’re trying to match a text pattern using regular expressions, but it is identifying the
 longest possible matches of a pattern. Instead, you would like to change it to find the
 shortest possible match. for regex: practise: please visit : https://regex101.com/
 Eg: match the string enclosed inside " "
 'Computer says "no."' ==> [no.]
 'Computer says "no." Phone says "yes."' ==> ['no.', 'yes.'] (correct answer) 
['no." Phone says "yes.'] -> this is wrong

'''

'''
. matches any character except a newline.
+ matches one or more of the preceding token.
? makes it non-greedy (shortest possible match).
'''
import re
text1 = 'Computer says "no."'
text2 = 'Computer says "no." Phone says "yes."'
pattern = r'"(.*?)"'   # this will find shortest one excluding Phone says from text2, it goes for non greedy approach
matches1 = re.findall(pattern, text1)
matches2 = re.findall(pattern, text2)
print(f"Matches in text1: {matches1}")      
print(f"Matches in text2: {matches2}")  
