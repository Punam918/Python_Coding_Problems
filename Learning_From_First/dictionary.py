data = {i: i**2 for i in range(10)}
print(data)

original = {'a': 1, 'b': 2, 'c': 3}
swapped = {v: k for k, v in original.items()}
print(swapped)


data = {i: i**2 for i in range(10) if i % 2 == 0}
print(data)


keys = ['name', 'age', 'city']
values = ['Alice', 25, 'New York']

data = {k: v for k, v in zip(keys, values)}
print(data)


names = ['Alice', 'Bob', 'Charlie']
data = {i: name for i, name in enumerate(names)}
print(data)


keys = ['a', 'b', 'c']
values = [1, 2, 3]

data = {v: k for k, v in zip(keys, values)}
print(data)


keys = ['one', 'two', 'three']
values = [1, 2, 3]

data = {k: v**2 for k, v in zip(keys, values)}
print(data)


dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'x': 10, 'y': 20, 'z': 30}

merged = {k: v for k, v in zip(dict1.keys(), dict2.values())}
print(merged)
