cost_price = int(input('Enter cost price-'))
selling_price = int(input('Enter selling price-'))

if cost_price < selling_price:
    print('Profit')
elif cost_price > selling_price:
    print('Loss')
else:
    print('No Loss No Gain')