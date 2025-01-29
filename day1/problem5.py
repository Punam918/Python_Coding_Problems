protfolio = [
 {'name': 'ABC', 'shares': 100, 'price': 91.1}, 
    {'name': 'DEF', 'shares': 50, 'price': 543.22}, 
    {'name': 'FB', 'shares': 200, 'price': 21.09}, 
    {'name': 'ABC', 'shares': 300, 'price': 305}
 ]

#Minimum
largest = sorted(protfolio,key = lambda x : x['price'],reverse=True)[:1]

#Maximum
smalllest = sorted(protfolio,key = lambda x:x['price'])[:1]

#Sorting
sorted_data = sorted(protfolio,key = lambda x:x['price'])

print(largest)
print(smalllest)
print(sorted_data)
