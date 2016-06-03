[← Return to Index](https://github.com/cjmlgrto/fit2085-notes/)

# Array Implementations of ADTs

## Lists
A sequence of items.

### List Operations
- Create list (initialise instance variables)
- Return list length
- Check if empty
- Check if full
- Add item (if not full)
- Delete item at position (shift all items after position over it)

```python
class List:
    def __init__(self, size):
        if size > 0:
            self.the_array = size * [None]
            self.count = 0
    
    def length(self):
        return self.count
        
    def is_empty(self):
        return self.count == 0
        
    def is_full(self):
        return self.count >= len(self.the_array)
        
    def add(self, new_item):
        has_space_left = not self.is_full()
        if has_space_left:
            self.the_arrray[self.count] new_item
            self.count += 1
        return has_space_left
        
    def delete(self, index):
        valid_index = index >= 0 and index < self.count
        if valid_index:
            for i in range(index, self.count-1):
                self.the_array[i] = self.the_array[i+1]
            self.count -= 1
        return valid_index
```

## Sorted Lists
A sequence of items in increasing order.

### Sorted List Operations
- Create list (initialise instance variables)
- Return list length
- Check if empty
- Check if full
- Add item (if there is space, find the correct position then make room by shifting all items after it)

```python
class SortedList:
    def __init__(self, size):
        if size > 0:
            self.the_array = size * [None]
            self.count = 0
    
    def length(self):
        return self.count
        
    def is_empty(self):
        return self.count == 0
        
    def is_full(self):
        return self.count >= len(self.the_array)
        
    def add(self, new_item):
        # if the list is empty, just insert
        if self.is_empty():
            self.the_array[self.count] = new_item
            self.count += 1
            return True
            
        # if it is not empty, find the correct position
        has_space_left = not self.is_full()
        if has_space_left:
            index = 0
            while index < self.count and new_item > self.the_array[index]
                index += 1
            
            # shift all items after indexx
            for i in range(self.count-1, index-1, -1):
                self.the_array[i + 1] = self.the_array[i]
            
            # insert item
            self.the_array[index] = new_item
            self.count += 1
        return has_space_left   
        
```

## Stacks
A list that follows the **LIFO** (Last-In, First-Out) model when inserting and retrieving items.

### Stack Operations
- Create a new stack (initialise instance variables: an array, counter, and pointer to top of stack)
- Return size
- Check if empty
- Check if full
- Push/add an item on top
- Pop/remove the item on top
- Peek/return at the item on top

```python
class Stack:
    # complexity of creating an array is O(N)
    def __init__(self, size):
        assert size > 0, "Size should be positive!"
        self.the_array = size * [None]
        self.count = 0
        self.top = -1
        
    # complexity is O(1) for all these methods
    
    def size(self):
        return self.count
        
    def is_empty(self):
        return self.size() == 0
        
    def is_full(self):
        return self.size() >= len(self.the_array)
        
    def push(self, new_item):
        if self.is_full():
            raise Exception("The stack is full!")
        self.top += 1
        self.the_array[self.top] = new_item
        self.count += 1
        
    def pop(self):
        if self.is_empty():
            raise Exception("The stack is empty!")
        item = self.the_array[self.top]
        self.top -= 1
        self.count -= 1
        return item
        
    def peek(self):
        if self.is_empty():
            raise Exception("The stack is empty!")
        item = self.the_array[self.top]
        return item
```

## Linear Queues

Lists that follow the **FIFO** (First-In, First-Out) model when inserting and retrieving items.

### Linear Queue Operations
- Create a queue
- Check if full
- Check if empty
- Reset the queue
- Append an item
- Serve an item

```python
class Queue:
    def __init__(self, size):
        assert size > 0, "Size should be positive!"
        self.the_array = size * [None]
        self.count = 0
        self.rear = 0
        self.front = 0
        
    def is_full(self):
        return self.rear >= len(self.the_array)
    
    def is_empty(self):
        return self.count == 0
        
    def reset(self):
        self.front = 0
        self.rear = 0
        self.count = 0
        
    def append(self, new_item):
        if self.is_full():
            raise Exception("Queue is full!")
        self.the_array[self.rear] = new_item
        self.rear += 1
        self.count += 1
    
    def serve(self):
        if self.is_empty():
            raise Exception("Queue is empty!")
        item = self.the_array[self.front]
        self.front += 1
        self.count -= 1
        return item
```

## Circular Queues

Lists that follow the **FIFO** (First-In, First-Out) model when inserting and retrieving items— but are less wasteful by wrapping the front and rear indices around the array.

### Circular Queue Operations
- Create a queue
- Check if full
- Check if empty
- Reset the queue
- Append an item
- Serve an item
- Print items in queue's order

```python
class Queue:
    def __init__(self, size):
        assert size > 0, "Size should be positive!"
        self.the_array = size * [None]
        self.count = 0
        self.rear = 0
        self.front = 0
        
    # notice that it tracks the count instead of the rear
    def is_full(self):
        return self.count >= len(self.the_array)
    
    def is_empty(self):
        return self.count == 0
        
    def reset(self):
        self.front = 0
        self.rear = 0
        self.count = 0
        
    def append(self, new_item):
        if self.is_full():
            raise Exception("Queue is full!")
        self.the_array[self.rear] = new_item
        self.rear = (self.rear + 1) % len(self.the_array)
        self.count += 1
    
    def serve(self):
        if self.is_empty():
            raise Exception("Queue is empty!")
        item = self.the_array[self.front]
        self.front = (self.front + 1) % len(self.the_array)
        self.count -= 1
        return item
        
    def print_items(self):
        index = self.front
        for _ in range(self.count):
            print(str(self.the_array[index]))
            index = (index + 1) % len(self.the_array)
```