squares = [x**2 for x in range(5)]
print(squares)  

even_numbers = [x for x in range(10) if x % 2 == 0]
print(even_numbers) 

nested_list = [[1, 2], [3, 4], [5, 6]]
flattened = [item for sublist in nested_list for item in sublist]
print(flattened) 


