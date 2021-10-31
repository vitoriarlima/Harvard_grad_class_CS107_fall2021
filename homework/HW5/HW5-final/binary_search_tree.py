#!/usr/bin/python3


class BSTNode:

    def __init__(self, key, val):
        self.key, self.val = key, val
        self.left = None
        self.right = None
        self.size = 1

    def __str__(self):
        return f'BSTNode({self.key}, {self.val})' + \
               '\n|\n|-(L)->' + '\n|      '.join(str(self.left ).split('\n')) + \
               '\n|\n|-(R)->' + '\n|      '.join(str(self.right).split('\n'))


class BSTTable:
    def __init__(self):
        self._root = None

    def __str__(self):
        return str(self._root)

    def __len__(self):
        return self._size(self._root)

    def put(self, key, val):
        self._root = self._put(self._root, key, val)

    def get(self, key):
        return self._get(self._root, key)

    def _put(self, node, key, val):
        if node is None:
            return BSTNode(key,val) 
        elif key == node.key:
            node.val = val
        elif node.key < key:
            node.right = self._put(node.right, key, val)
        else: #node.key > key :
            node.left = self._put(node.left, key, val)
        
        node.size = self._size(node.right) + self._size(node.left) + 1
        return node
    
    def _get(self, node, key):
        if node is None:
            raise KeyError("The node with key", key, "doesn't exist yet, create one before")
        elif node.key == key:
            return node.val
        elif node.key < key:
            return self._get(node.right, key)
            #return node.right.val
        else: #node.key > key :
            return self._get(node.left, key)
        #return node.left.val
        #pass # TODO

    @staticmethod
    def _size(node):
        return node.size if node else 0
    
    # The put method inserts a key-value pair into the BSTTable. 
    # It delegates the function call to _put. Please implement the non-public 
    # method _put. It takes a node, a key, and a val as arguments. node is the root of 
    # the subtree into which the key-value pair is to be inserted. After the insertion, 
    # the root of this subtree may change. _put should return the new root of this subtree. 
    # The difference of the input subtree and the returned subtree is that in the returned 
    # subtree, a new key-value pair has been inserted. If the key was already in the subtree, 
    # then we update the value of the corresponding node.


greektoroman = BSTTable()
print(greektoroman.put('Athena',    'Minerva'))
print(greektoroman.put('Eros',      'Cupid'))
print(greektoroman.put('Aphrodite', 'Venus'))
print(greektoroman.get('Eros'))
print(greektoroman.get('Vitoria'))
print(greektoroman.get('Lala'))

print (greektoroman)