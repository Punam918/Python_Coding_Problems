'''
Write a Python program to sort a list of nested dictionaries.

'''
dicti =[{'key': {'subkey': 1}}, {'key': {'subkey': 10}}, {'key': {'subkey': 5}}]

for items in dicti:
    dictsort = sorted(dicti,key = lambda x:x['key']['subkey'])    
print(dictsort)
