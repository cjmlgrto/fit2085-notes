[← Return to Index](https://github.com/cjmlgrto/fit2085-notes/)

# Priority Queues

## Priority Queues
- Just like a queue, but each element has a numeric _priority_
- Element with the **highest priority number** is processed first
- Operations are _append_ and _serve_— which serves the high priority element
- Arrays, linked lists, binary search trees and heaps can be used as the underlying data structure

### Using Linear Structures

| Implementation | Serve | Insert |
| --- | :---: | :---: |
| Unsorted array | O(n) | O(1) |
| Unsorted linked list | O(n) | O(1) |
| Sorted array | O(1) | O(n) |
| Sorted linked list | O(1) | O(n) |

### Using a Binary Search Tree
Serving and inserting complexities are O(log n) best case, or O(n) worst case

```python
class BinarySearchTree:
    # ...
    
    def get_max(self):
        if self.root is None:
            raise ValueError("Priority Queue is empty!")
        elif self.root.right is None: # root has max
            temp = self.root.item
            self.root = self.root.left # delete root
            return temp
        else:
            return self.get_max_aux(self.root.right, self.root)
            
    def get_max_aux(self, current, parent):
        if current.right is None: # base case: at max
            parent.right = current.left
            return current.item
        else:
            return self.get_max_aux(current.right, current)
```