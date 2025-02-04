'''
Write a Python program to find the list of words that are longer than n from a given list of words.
e.g. : from 'The quick brown fox jumps over the lazy dog' -> ['quick', 'brown', 'jumps', 'over', 'lazy']
'''

stringg = 'The quick brown fox jumps over the lazy dog'
n=3
count = 0

for word in stringg.split():
    if len(word)>3:
        count+=1
        print(word, end = " ")        
print(count)