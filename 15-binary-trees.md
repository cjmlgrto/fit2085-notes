[← Return to Index](https://github.com/cjmlgrto/fit2085-notes/)

# Binary Trees

## Trees
- Are simple, connected graphs with no circuits
- Contains a parent node and children node
- A node with no parent is the _root_
- A node with no child is a _leaf_
- Every node that is not a leaf is a _parent_
- Every node is the root node of its _subtree_
- Every node except the root is a _child_
- The _height_ or depth of a tree is its maximum _level_
- The _width_ is the number of nodes in the level with the highest number of nodes
- **Binary Trees** have at most _two_ children

## Binary Trees
- Trees where very node has at most _two_children
- For a **perfect binary tree** of height k, there are 2<sup>k</sup> leaves, and **2<sup>k+1</sup>-1** nodes
- With N nodes, the height of a perfect binary tree is O(log N)
- The height of an unbalanced tree is O(N)

### Accessing Items
- Requires two values: the item, and a bitstring
- The bitstring represents where the item is to be stored, where `0` represents **left** and `1` represents **right**

### Recursively Traversing All Items
- **Preorder**: access the root, then the left subtree, then the right subtree
- **Inorder**: access the left subtree, the root, then the right subtree
- **Postorder**: access the left subtree, the right subtree, then the root

### Computing the Size
- Recursively determine the length of each subtree
- ``size(self) = size(left) + 1 + size(right)``

### Python Implementation of a Binary Tree Object
```python
class TreeNode:
	def __init__(self, item, left, right):
		self.item = item
		self.right = right
		self.left = left

class BinaryTree:
	def __init__(self):
		self.root = None

	def add(self, item, binary_str):
		binary_str_itr = iter(binary_str)
		self.root = self.add_aux(self.root, item, binary_str_itr)

	def add_aux(self, current, item, binary_str_itr):
		if current is None:
			current = TreeNode(None, None, None)
		try:
			bit = next(binary_str_itr)
			if bit == "0":
				current.left = self.add_aux(current.left, item, binary_str_itr)
			elif bit == "1":
				current.right = self.add_aux(current.right, item, binary_str_itr)
		except StopIteration:
			current.item = item
		return current

	def get(self, binary_str):
		binary_str_itr = iter(binary_str)
		return self.get_aux(self.root, binary_str_itr)

	def get_aux(self, current, binary_str_itr):
		try:
			bit = next(binary_str_itr)
			if bit == '0':
				return self.get_aux(current.left, binary_str_itr)
			elif bit == '1':
				return self.get_aux(current.right, binary_str_itr)
		except StopIteration:
			try:
				return current.item
			except:
				print("No item exists here!")

	def print_inorder(self):
		self.print_inorder_aux(self.root)
		print("")

	def print_inorder_aux(self, current):
		if current is not None:
			self.print_inorder_aux(current.left)
			if current.item is not None:
				print(current.item,end="")
			self.print_inorder_aux(current.right)
			
	def __len__(self):
	    return self.len_aux(self.root)
	    
	def len_aux(self, current):
	    if current is None:
	        return 0
	    else:
	        return 1 + self.len_aux(current.left) + self.len_aux(current.right)
	        
	def get_leaves(self, current):
	    a_list = []
	    self.get_leaves_aux(self.root, a_list)
	    return a_list
	    
	def get_leaves_aux(self, current, a_list):
	    if current is not None:
	        if self.is_leaf(current):
	            a_list.append(current.item)
	        else:
	            self.get_leaves_aux(current.left, a_list)
	            self.get_leaves_aux(current.right, a_list)
	
	def is_leaf(self, current):
	    return current.left is None and current.right is None
```

## Expression Trees
- Are binary trees buit with operators (inner nodes) and operands (leaves)
- Also known as a _parse_ tree (used to figure out if an expression is 'valid', used in compilers and other applications)
- **Preorder traversal**: Prefix notation
- **Inorder**: Infix noation
- **Postorder**: Postfix notation
    