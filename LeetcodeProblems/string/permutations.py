import itertools

s = "GFG"
li = [''.join(p) for p in itertools.permutations(s)]
print(li)
