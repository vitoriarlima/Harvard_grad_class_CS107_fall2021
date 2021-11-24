from math import floor
from typing import List
import numpy as np 


class Heap:
    def __init__(self, array: List[int]) -> None:
        self.elements = array
        self.size = len(array) # Number of elements in heap
        self.build_heap()

    # index of left child of the node at idx
    def left(self, idx: int) -> int:
        return 2 * idx + 1

    # index of right child of the node at idx
    def right(self, idx: int) -> int:
        return 2 * idx + 2

    def parent(self, idx: int) -> int:
        return floor((idx - 1) / 2)

    def swap(self, idx1: int, idx2: int) -> None:
        tmp = self.elements[idx1]
        self.elements[idx1] = self.elements[idx2]
        self.elements[idx2] = tmp

    def to_string(self, prefix: str = "", idx: int = 0, left: bool = False) -> str:
        if self.size == 0:
            return '\\--'
        elif idx < self.size:
            buf = prefix
            if left:
                buf = buf + "|-- "
            else:
                buf = buf + "\\-- "
            buf = buf + '\033[1m' + str(self.elements[idx]) + '\033[0m' + '\n'
            #buf = buf + str(self.elements[idx]) + '\n' #use if above doesn't work

            new_prefix = prefix
            if left:
                new_prefix = new_prefix + "|   "
            else:
                new_prefix = new_prefix + "    "

            return buf + \
                    self.to_string(new_prefix, self.left(idx), True) + \
                    self.to_string(new_prefix, self.right(idx), False)
        else:
            return ''

    def __str__(self) -> str:
        return self.to_string()

    def __len__(self) -> int:
        return self.size
    
    def compare(self, a: int, b: int) -> bool:
        raise NotImplementedError
        

    def heapify(self,idx: int) -> None:
        if idx >= self.size: 
            return    
        current = idx
        left = self.left(idx)
        right = self.right(idx)
        if left < self.size and self.compare(self.elements[left], self.elements[current]):
            current = left
        
        if right < self.size and self.compare(self.elements[right], self.elements[current]):
            current = right
            
        if current != idx:
            self.swap(idx, current)
            #self.elements[idx], self.elements[current] = self.elements[current], self.elements[idx]
            self.heapify(current)
        
        
    def build_heap(self) -> None:
        # TODO: implement
        n = int((len(self.elements)//2)-1)
        for k in range(n, -1, -1):
            self.heapify(k)
    
    def heappush(self, key: int) -> None:

        def _help_heap(idx):
            current = self.elements[idx]
            parent = self.parent(idx)
            while self.compare(self.elements[idx], self.elements[parent]) and idx != 0:
                self.swap(idx, parent) # swapping the values
                idx = parent
                parent = self.parent(parent)
            self.elements[idx] = current
            
        self.elements.append(key)
        self.size += 1
        #need to do minus 1 because index starts at zero
        _help_heap((self.size-1))
        
    def heappop(self) -> int:        
        if self.size ==0:
            raise indexError("This is an empty heap")
        else:
            self.elements[0], self.elements[-1] = self.elements[-1], self.elements[0]
            deleted = self.elements.pop()
            self.size -=1
            self.heapify(0)
            return f"Removed Element: {deleted}"
    
    
class MinHeap(Heap):
    def compare(self, a: int, b: int) -> bool:
        if (b>a):
            return True
        
        else: 
            return False

class MaxHeap(Heap):
    def compare(self, a: int, b:int) -> bool:
        if(a>b):
            return True
        else:
            return False
    
"""
##############
# Test code
#############

h = MinHeap([-1,0,0,15,23,1,2,3]) 
print(h)

h = MaxHeap([-1,0,0,15,23,1,2,3]) 
print(h)

h = MaxHeap([1,2,3,4,5]) 
print(h)

h = MinHeap([1,2,3,4,5]) 
print(h)

print(h.elements) #from left to right

j = MinHeap([])
j.heappush(-1)
j.heappush(6)
j.heappush(10)
j.heappush(7)
j.heappush(0)
print(j.elements)
print(j.size)
print(j)

j = MaxHeap([])
j.heappush(-1)
j.heappush(6)
j.heappush(10)
j.heappush(100)
j.heappush(10000)
print(j.elements)
print(j.size)
print(j)

j = MinHeap([])
j.heappush(-1)
j.heappush(0)
j.heappush(0)
j.heappush(15)
print(j.elements)
print(j.size)
print(j)

print(j.elements)
j.heappop()
print(j.elements)
print(j.size)
print(j)

j = MinHeap([])
j.heappush(-1)
j.heappush(0)
j.heappush(0)
j.heappush(15)
j.heappush(23)
j.heappush(1)
j.heappush(2)
j.heappush(3)
print(j.elements)
print(j.size)
print(j)

print(j.elements)
j.heappop()
print(j.elements)
print(j.size)
print(j)"""