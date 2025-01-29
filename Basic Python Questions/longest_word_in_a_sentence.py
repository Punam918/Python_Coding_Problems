def longest_word(sent):
    words = sent.split()
    return max(words,key = len)
value = str(input("enter a sentence"))
print(longest_word(value))