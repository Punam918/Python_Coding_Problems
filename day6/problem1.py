'''
Write a Python program to count the number of strings from a given list of strings. The string length is 2 or more and the first and last characters are the same.
Sample List : ['abc', 'xyz', 'aba', '1221']
Expected Result : 2
aba and 1221 are the one with first and last character same
'''
list = ['abc', 'xyz', 'aba', '1221']
count = 0
for item in list:
    if item[0] == item[-1]:
        count+=1
print(count)

list = ['abc', 'xyz', 'aba', '1221']
count = 0
for item in list:
    if len(item)>1 and item[0]==item[-1]:
        count+=1
print(count)
    