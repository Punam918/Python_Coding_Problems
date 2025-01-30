""" 
Filter a list of numbers using a generator expression. create a generator expression to yield only the 
even numbers from the list.
"""
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#This is generator exprssions, we don't need to use yield in generator expressions
even_numbers = (num for num in numbers if num % 2 == 0)
for num in even_numbers:
    print(num, end=" ")


# generator is created using python functions and it has yield also 
def even_generator(nums):
    for num in nums:
        if num % 2 == 0:
            yield num  

numbers = [2,3,4,5,6,7]
even_numbers = even_generator(numbers)

for num in even_numbers:
    print(num, end=" ")
