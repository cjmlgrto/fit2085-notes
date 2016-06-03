class BinarySearchTreeNode:
    def __init__(self, key, item=None, left=None, right=None):
        self.key = key
        self.item = item
        self.left = left
        self.right = right

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def is_empty(self):
        return self.root is None

    def __getitem__(self, key):
        return self.getitem_aux(self.root, key)

    def _getitem_aux(self, current, key):
        if current is None: # base case: empty
            raise KeyError("Key not found")
        elif key == current.key # base case: found
             return current.item
         elif key < current.key:
             return self._getitem_aux(current.left, key)
         else:
             return self._getitem_aux(current.right, key)

     def insert(self, key, item):
         self.root = self._insert_aux(self.root, key, item)

     def _insert_aux(self, current, key, item):
         if current is None: # base case: at the leaf
             current = BinarySearchTreeNode(key, item)
         elif key < current.key:
             current.left = self._insert_aux(current.left, key, item)
         elif key > current.key:
             current.right = self._insert_aux(current.right, key, item)
         else: # key == current.key
             raise ValueError("Duplicate Item")
         return current

     def __setitem__(self, key, item):
         self.root = self._insert_aux(self.root, key, item)

     def _setitem_aux(self, current, key, item):
         if current is None: # base case: at the leaf
             current = BinarySearchTreeNode(key, item)
         elif key < current.key:
             current.left = self._setitem_aux(current.left, key, item)
         elif key > current.key:
             current.right = self._setitem_aux(current.right, key, item)
         else: # key == current.key
             current.item = item
         return current

     def __delitem__(self, key):
         # left as an exercise
         pass