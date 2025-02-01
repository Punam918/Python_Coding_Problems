'''
You want to pick random items out of a sequence or generate random numbers., shuffle them, use 
seed . 
'''
import random
random.seed(42)
random_num = random.randint(1, 100)  
print(f"Random Number: {random_num}")

sequence = ['apple', 'banana', 'cherry', 'date']
random_item = random.choice(sequence)
print(f"Random Item: {random_item}")

random.shuffle(sequence)
print(f"Shuffled Sequence: {sequence}")

random_items = random.sample(sequence, 2)  
print(f"Random Items: {random_items}")

random_float = random.random()
print(f"Random Float: {random_float}")
