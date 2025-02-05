'''Accept the strings which contains all vowels'''
a = 'aaee uuaa ooii aeiou ccddae'
b = []
for word in a.split():
    if all(vowel in word for vowel in 'aeiou'):
        b.append(word)            
print(" ".join(b))
    


