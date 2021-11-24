from enum import Enum

class BSTNode:

    def __init__(self, key, val):
        self.key, self.val = key, val
        self.left, self.right = None, None
        self.size = 1

    def __str__(self):
        return f'BSTNode({self.key}, {self.val})' + \
               '\n|\n|-(L)->' + '\n|      '.join(str(self.left ).split('\n')) + \
               '\n|\n|-(R)->' + '\n|      '.join(str(self.right).split('\n'))
    
    def __repr__(self):
        return f"{self.key}, {self.val}"

class BSTTable:
    def __init__(self):
        self._root = None

    def __str__(self):
        return str(self._root)

    def __len__(self):
        return self._size(self._root)

    def min(self,node):
        if node.left != None:
            node.left = self.min(node.left)
        return node

    def put(self, key, val):
        self._root = self._put(self._root, key, val)

    def get(self, key):
        return self._get(self._root, key)

    def _put(self, node, key, val):
        if not node: 
            return BSTNode(key, val)
        if   key < node.key:
            node.left  = self._put(node.left,  key, val)
        elif key > node.key:
            node.right = self._put(node.right, key, val)
        else:
            node.val = val
        node.size = 1 + self._size(node.left) + self._size(node.right)
        return node

    def _get(self, node, key):
        if not node:
            raise KeyError(f'key not found: {key}')
        if   key < node.key:
            return self._get(node.left,  key)
        elif key > node.key:
            return self._get(node.right, key)
        else:
            return node.val

    @staticmethod
    def _size(node):
        return node.size if node else 0
    
    ####### PART A
    def _removemin(self, node):
        if not node.left: #if node.left == None:
            return node.right
        else: #this means that it still has left nodes and that it s still not the minimum
            node.left = self._removemin(node.left)
            node.size = 1 + self._size(node.left) + self._size(node.right) #number of nodes
            return node #subtree with the smallest node (the node with the smallest key) removed
    
    ###### PART B
    def remove(self, key):
        self._root = self._remove(self._root, key)
         
    def _remove(self, node, key):
        #TODO: Should return a subtree whose root is <node> but without
        #      the node whose key is <key>
        ### SLIDE 34 - pseudo code from Hibbard Deletion
        
        if node == None :
            raise KeyError(f"The key has not been found, key: {key}")
        
        #traversing
        if key > node.key:
            node.right = self._remove(node.right, key)
            
        #traversing
        elif key < node.key:
            node.left = self._remove(node.left, key)
        
        
        else: # key = node.key
            # 0 or 1 child, if there is 1 child it s at the left
            if node.right == None:
                return node.left
            # 0 or 1 child, if there is one child it s at the right
            if node.left == None:
                return node.right
            # case where a node has 2 kids
            else: 
        
                node_t = node
                node = self.min(node_t.right) #this is the smallest at the right
                node.right = self._removemin(node_t.right)
                node.left = node_t.left

        node.size = 1 + self._size(node.left) + self._size(node.right)
        return node


class DFSTraversalTypes(Enum):
    PREORDER = 1
    INORDER = 2
    POSTORDER = 3

class DFSTraversal():
    def __init__(self, tree: BSTTable, traversalType: DFSTraversalTypes):
        # TODO: implement
        self.tree = tree
        self.traversalType = traversalType
        self.my_list = []
        self.current_index = 0
        if self.traversalType == self.traversalType.INORDER: 
            self.inorder(self.tree)
        elif self.traversalType == self.traversalType.PREORDER:
            self.preorder(self.tree)
        elif self.traversalType == self.traversalType.POSTORDER:
            self.postorder(self.tree)
    

    def __iter__(self):
        # TODO: implement
        return self    ##### returns only SELF


    def __next__(self):
        # TODO: implement
        ## This returns next element
        ###### self.current _index : RETURN IT AND INCREMENT IT
        ## It tracks the index of where I am at
        ## When you call next the first time is 0, 
        # then the second time is 1, and so on, and increment it every time
        ## If your current index is largere, then raise at STOP ITERATION ERROR
        if self.current_index>= len(self.my_list):
            raise StopIteration("Now you exhausted the iterator (your list) length")
        else:
            index_at_this_iteration = self.current_index
            self.current_index +=1
            return self.my_list[index_at_this_iteration]
                
    def _inorder(self, node):
        if node == None:
            return
        else:
            self._inorder(node.left)
            self.my_list.append(node)
            self._inorder(node.right) 
                 
    def inorder(self, bst: BSTTable):
        return self._inorder(bst._root)
        
    def _preorder(self, node):
        if node == None:
            return
        else:
            self.my_list.append(node)
            self._preorder(node.left)
            self._preorder(node.right)

    def preorder(self, bst: BSTTable):
        return self._preorder(bst._root)
    
    def _postorder(self, node):
        if node == None:
            return
        else:
            self._postorder(node.left)
            self._postorder(node.right)
            self.my_list.append(node)

    def postorder(self, bst: BSTTable):
        return self._postorder(bst._root)

"""
##############
# Test cases #
##############

# DEMO PART A
tree = BSTTable()
tree.put(0, 'd')
tree.put(2, 'c')
tree.put(5, 'a')
tree.put(1, 'b')
print(tree._root)
print("--------")
print(tree._removemin(tree._root))

# DEMO PART B
tree = BSTTable()
tree.put(5, 'a')
tree.put(1, 'b')
tree.put(2, 'c')
tree.put(0, 'd')
tree.remove(5)
print(tree)
tree.remove(1)
print(tree)

# This shall return a key error
#tree.remove(10)

######################
# Traversal test codes
######################
input_array = [(4, 'a'), (9, 'c'), (2, 'f'), (3, 'z'), (11, 'i'), (8, 'r')]
bst = BSTTable()
for key, val in input_array:
    bst.put(key, val)
print(bst)

#################
# next(traversal) will work up to when the list if finished
##################
traversal = DFSTraversal(bst, DFSTraversalTypes.POSTORDER)
next(traversal)

traversal = DFSTraversal(bst, DFSTraversalTypes.POSTORDER)
for node in traversal:
    print(str(node.key) + ', ' + node.val)

traversal = DFSTraversal(bst, DFSTraversalTypes.INORDER)
for node in traversal:
    print(str(node.key) + ', ' + node.val)

traversal = DFSTraversal(bst, DFSTraversalTypes.PREORDER)
for node in traversal:
    print(str(node.key) + ', ' + node.val)"""


