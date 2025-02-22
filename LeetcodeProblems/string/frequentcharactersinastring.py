from collections import Counter
s = 'punamisverygoodgirlmisv'
freq = Counter(s)
res = max(freq,key =freq.get)
resmin = min(freq,key = freq.get)
print(resmin)
print(res)