#  Eg_2 = protfolio = [
#  {'name': 'ABC', 'shares': 100, 'price': 91.1}, 
#     {'name': 'DEF', 'shares': 50, 'price': 543.22}, 
#     {'name': 'FB', 'shares': 200, 'price': 21.09}, 
#     {'name': 'ABC', 'shares': 300, 'price': 305}
#  ]
#  find the largest and smallest three portfolios based on their price.   
protfolio = [
 {'name': 'ABC', 'shares': 100, 'price': 91.1}, 
    {'name': 'DEF', 'shares': 50, 'price': 543.22}, 
    {'name': 'FB', 'shares': 200, 'price': 21.09}, 
    {'name': 'ABC', 'shares': 300, 'price': 305}
 ]
largest_portfolios = sorted(protfolio, key=lambda x: x['price'], reverse=True)[:3]
smallest_portfolios = sorted(protfolio, key=lambda x: x['price'])[:3]

print("\nLargest 3 portfolios by price:", largest_portfolios)

print("Smallest 3 portfolios by price:", smallest_portfolios)