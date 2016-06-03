[← Return to Index](https://github.com/cjmlgrto/fit2085-notes/)

# Iterators and Generators

## Iterators

### Iterables
- Are items that can be 'iterated' over— like lists, strings, or even the lines of a file.
- The `for` keyword is used when iterating over _iterables_.

```python
for item in [1, 2, 3]:
    print(item)
>>> 1
>>> 2
>>> 3

for character in "dog":
    print character
>>> d
>>> o
>>> g
```

### Behind The Scenes
- The `for` keyword tells Python to use the built-in `iter()` function
- The `iter()` function takes an iterable object, and returns an iterator— a class that allows to manipulate the iterable object

```python
x = iter([1, 2, 3])
x.next()
>>> 1
x.next()
>>> 2
x.next()
>>> 3
x.next()
>>> Error!
```
Which can be manually implemented as a class by yourself:

```python
class ListIterator:
    def __init__(self, head):
        self.current = head
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.current is None:
            raise StopIteration
        else:
            item_required = self.current.item
            self.current = self.current.next
            return item_required
```

And can be used by iterable objects and clasess that you define— for example, in the **Linked List**:

```python
class LinkedList:
    # ...
    
    def __iter__(self):
        return ListIterator(self.head)
     
    # ...
```
    
Through this, you can then use the `for` keyword in your own custom-defined **Linked List** class:

```python
# ...
linked_list = LinkedList()
# ...
for item in linked_list:
    print(item)
# ...
```

## Generators
Cool tricks you can do with the `for` keyword:

```python
A = [3*x for x in range(5)]
print(A)
>>> [0, 3, 6, 9, 12]

B = [x for x in A if x % 2 == 0]
print(B)
>>> [0, 6, 12]
```

