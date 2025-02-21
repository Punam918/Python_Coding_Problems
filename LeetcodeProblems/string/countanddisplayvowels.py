# Count and display vowels in a string

vow = 'aeiouAEIOU'
s = str(input("enter a string/word/sentence"))

sumvow = sum(1 for char in s if char in vow)
print(sumvow)

for char in s:
    if char in vow:
        print(char)

