#!/usr/bin/env python

class Fibonacci():

    def __init__(self, length):
        self.length = length
        self.sequence = [0, 1]
        for i in range(length):
            self.sequence.append(sum(self.sequence[-2:]))

    def __getitem__(self, index):
        return self.sequence[index+2]

    def __len__(self):
        return len(self.sequence)

    def __iter__(self):
        return FibonacciIterator(self)

class FibonacciIterator():

    def __init__(self, fib, position=0):
        self.fib = fib
        self.position = position

    def __iter__(self):
        return self

    def __next__(self):
        if self.position >= self.fib.length:
            raise StopIteration
        else:
            self.position += 1
            return self.fib[self.position - 1]

fib = Fibonacci(10)
print(list(iter(fib)))
