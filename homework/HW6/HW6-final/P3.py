from math import floor
from typing import List
import numpy as np 
from P2 import MinHeap

from random import sample
from time import time


class PriorityQueue:
    def __init__(self, max_size):
        self.elements = []
        self.max_size = max_size

    def __len__(self):
        return len(self.elements)

    def __bool__(self):
        return len(self.elements) > 0

    def put(self, val):
        raise NotImplementedError 

    def get(self):
        raise NotImplementedError 

    def peek(self):
        raise NotImplementedError 

def mergesortedlists(lists, pqclass=PriorityQueue):
    merged = []
    pq = pqclass(len(lists))
    for i, l in enumerate(lists): 
        pq.put((l.pop(0), i))

    while pq:
        ele, i = pq.get()
        merged.append(ele)
        if lists[i]:
            pq.put((lists[i].pop(0), i)) 

    return merged


def generatelists(n, length=20, dictionary_path='data/words.txt'):
    with open(dictionary_path, 'r') as f:
        words = [w.strip() for w in f.readlines()]
    lists = []
    for _ in range(n):
        lists.append(sorted(sample(words, length)))
    return lists


def timeit(ns=(10, 20, 50, 100, 200, 500), pqclass=PriorityQueue, n_average=5):
    elapsed = []
    for n in ns:
        timeaccum = 0
        for _ in range(n_average):
            lists = generatelists(n)
            start = time()
            merged = mergesortedlists(lists, pqclass)
            end   = time()
            timeaccum += end-start
        elapsed.append(timeaccum / n_average)
    return elapsed


class NaivePriorityQueue(PriorityQueue):
    def __init__(self, max_size):
        super().__init__(max_size)

    def __len__(self):
        return len(self.elements)
    
    def __bool__(self):
        return len(self.elements) > 0
        
    def put(self, val):
        if len(self.elements) == self.max_size:
            raise IndexError(f"maximum size of priority Queue {self.max_size} has been reached")
        else:
            self.elements.append(val)
    def get(self):
        if len(self.elements)==0:
            raise IndexError(f"Queue is Empty")
        else:
            min_val= min(self.elements)
            new_self_elements= []
            for i in range(0, len(self.elements)):
                if self.elements[i] != min_val:
                    new_self_elements.append(self.elements[i])
            self.elements=new_self_elements
            return min_val
                
    def peek(self):
        if len(self.elements)==0:
            raise IndexError(f"Queue is Empty")
        else:
            min_val= min(self.elements)
            return min_val

    def __str__(self):
        return f" The current priority queue is {self.elements}"

class HeapPriorityQueue(PriorityQueue): #min proprity, min heap
    def __init__(self, max_size):
        super().__init__(max_size)
        self.elements = MinHeap([])
        
    def put(self, val):
        if len(self.elements) == self.max_size:
            raise AttributeError(f"maximum size of priority Queue {self.max_size} has been reached")
        else:
            self.elements.heappush(val)
    
    def get(self):
        if len(self.elements)==0:
            raise AttributeError(f"Queue is Empty")
        else:
            root= self.elements.elements[0]
            self.elements.heappop()
            return root
                    
    def peek(self):
        if len(self.elements)==0:
            raise AttributeError(f"Queue is Empty")
        else:
            root= self.elements.elements[0]
            return root

import heapq

class PythonHeapPriorityQueue(PriorityQueue): 
    def __init__(self, max_size):
        super().__init__(max_size)
        
    def put(self, val):
        if len(self.elements) == self.max_size:
            raise AttributeError(f"maximum size of priority Queue {self.max_size} has been reached")
        else:
            heapq.heappush(self.elements, val)
    
    def get(self):
        if len(self.elements)==0:
            raise AttributeError(f"Queue is Empty")
        else:
            root= self.elements[0]
            heapq.heappop(self.elements)
            return root
                
    def peek(self):
        if len(self.elements)==0:
            raise AttributeError(f"Queue is Empty")
        else:
            root= self.elements[0]
            return root


"""
##############
# Test codes
#############

q = PythonHeapPriorityQueue(10)
q.put(1)
q.put(2)
print(q.peek())
print(q.get())
print(q.get())

q = HeapPriorityQueue(2)
q.put(1)
q.put(2)
print(q.peek())
print(q.get())
print(q.get())

q = NaivePriorityQueue(2)
q.put(1)
q.put(2)
print(q.peek())
print(q.get())
print(q.get())"""




def mergesortedlists(lists, pqclass=NaivePriorityQueue):
    merged = []
    pq = pqclass(len(lists))
    for i, l in enumerate(lists): 
        pq.put((l.pop(0), i))
    
    while pq:
        ele, i = pq.get()
        merged.append(ele)
        if lists[i]:
            pq.put((lists[i].pop(0), i)) 
    
    return merged


def generatelists(n, length=20, dictionary_path='data/words.txt'):
    with open(dictionary_path, 'r') as f:
        words = [w.strip() for w in f.readlines()]
    lists = []
    for _ in range(n):
        lists.append(sorted(sample(words, length)))
    return lists


def timeit(ns=(10, 20, 50, 100, 200, 500), pqclass=NaivePriorityQueue, n_average=5):
    elapsed = []
    for n in ns:
        timeaccum = 0
        for _ in range(n_average):
            lists = generatelists(n)
            start = time()
            merged = mergesortedlists(lists, pqclass)
            end   = time()
            timeaccum += end-start
        elapsed.append(timeaccum / n_average)
    return elapsed