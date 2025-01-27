from collections import Counter
sequence = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5]
counter = Counter(sequence)
most_common = counter.most_common()
print(most_common)
