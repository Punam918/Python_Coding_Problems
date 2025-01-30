"""
Create a custom iterator that iterates through a list of numbers and returns the squares of each number
when iterated.

"""

class SquareIterator:
    def __init__(self, numbers):
        self.numbers = numbers
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.numbers):
            result = self.numbers[self.index] ** 2
            self.index += 1
            return result
        else:
            raise StopIteration

numbers = [1, 2, 3, 4, 5]
square_iterator = SquareIterator(numbers)

for square in square_iterator:
    print(square)
