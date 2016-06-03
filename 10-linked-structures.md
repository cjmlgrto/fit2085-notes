[← Return to Index](https://github.com/cjmlgrto/fit2085-notes/)

# Linked Structures

## Non-Linked (Fixed) Structures

### Advantages
- Very fast, random access with O(1) complexity
- Very compact representation if array is full

### Disadvantages
- Non-resizable (max size is required on creation)
- Changing size is costly (creating a new array then copying all new items)
- Slow operations of shuffling elements is required

## Linked Structures

### Advantages
- Fast insertion and deletion (no need for shuffling)
- Easily resizable
- Never full (memory is the limit!)
- Less memory used if the "relatively empty"

### Disadvantages
- More memory used than a full array
- No random access

## Nodes
Are the basic building blocks of linked structures. They make deleting and adding items easier, and allows for dynamically-resizing data structures. 

Nodes are ADTs that contain:

- A value
- A pointer to the next node

```python
class Node:
    def __init__(self, item=None, next=None):
        self.item = item
        self.next = next
        
    def __str__(self):
        return str(self.item)
```

## Stacks with Linked Nodes
- Top of the stack is a reference to the latest created node
- Pushing and popping items is simply creating/deleting nodes then re-assigning the top pointer

```python
from node import Node

class Stack:
    def __init__(self):
        self.top = None
        
    def is_empty(self):
        return self.top is None
    
    def reset(self):
        self.top = None
        
    def push(self, item):
        self.top = Node(item, self.top)
        
    def pop(self):
        if self.is_empty():
            raise Exception("Stack is empty!")
        item = self.top.item
        self.top = self.top.next
        return item
```

## Queues with Linked Nodes

### Appending:
1. Create a new node
2. If queue is empty, set the front to the new node
3. Else, set the current rear's reference to the new node
4. Set the rear to this new node

### Serving:
1. If queue is empty, throw an exception
2. Remember the item in the front node
3. Make the next node the new front
4. If the new front is pointing to none, point the rear to none
5. Return the item

```python
from node import Node

class Queue:
    def __init__(self):
        self.front = None
        self.read = None
    
    def is_empty(self):
        return self.front is None
    
    def reset(self):
        self.front = None
        self.rear = None
    
    def append(self, item):
        new_node = Node(item, None)
        if self.is_empty():
            self.front = new_node
        else:
            self.rear.next = new_node
        self.rear = new_node
        
    def serve(self):
        if self.is_empty():
            raise Exception("Queue is empty!")
        temp = self.front.item
        self.front = self.front.next
        if self.front is None:
            self.rear = None
        return temp
```

## Linked Lists

### Getting the n-th Item

1. Create a reference called 'node' to the head node
2. Iterate n times, referencing the next node as 'node'

### Inserting at position i
1. If inserting at 0, set the head reference to a new node pointing to the last head node
2. Otherwise, get the (i-1)-th node, then set point it to a new node containing the new value, referencing the node next to the (i-1)-th node

```python
from node import Node

class List:
   def __init__(self):
       self.head = None
       self.count = 0
   
   def is_empty(self):
       return self.count == 0
       
   def reset(self):
       self.__init__()
       
   def __len__(self):
       return self.count
       
   def _get_node(self, index):
       if index < 0 or index > self.count:
           raise Exception("Index out of bounds!")
       node = self.head
       for _ in range(index):
           node = node.next
       return node
   
   def insert(self, index, item):
       index = index % len(self)
       if index == 0:
           self.head = Node(item, self.head)
       else:
           node = self._get_node(index-1)
           node.next = Node(item, node.next)
       self.count += 1
       
   def delete(self, index):
       if self.is_empty():
           raise IndexError("The list is empty!")
       if index < 0 or index >= len(self):
           raise IndexError("Index is out of range!")
       if index == 0:
           self.head = self.head.next
       else:
          node = self._get_node(index-1)
          node.next = node.next.next
       self.count -= 1
```
       