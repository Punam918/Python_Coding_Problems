'''

Iterable : list,tuple,set are iterable. An object that can return an iterator. that supports __iter__()
Iterator : It is used to fetch items from an iterable one at a time. Iterators implement the __next__() method, and once exhausted, it raises the StopIteration exception.
Iteration : In each iteration, getiing one iterable item from iterable.

'''
items = [1, 2, 3, 4, 5]
iterator = iter(items)
try:
    while True:
        item = next(iterator)
        print(item)
except StopIteration:
    pass
