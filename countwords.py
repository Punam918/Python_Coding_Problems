# no of words in a sentence
def count_words(word):
    wor = word.split()
    return len(wor)
val = str(input("ente a word"))
print(count_words(val))