'''Least Frequent Character in String'''
from collections import Counter
a = 'punam is a very good girl c'
b = Counter(a)
c = b.most_common()[-1]
print(c)