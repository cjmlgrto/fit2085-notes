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
A = (3*x for x in range(5))  #  Generator comprehension.
print(A)
>>> <generator object <genexpr> at 0x10c63a518>
for num in A:  # Iterate through items in generator.
    print(num, end=" ")
>>> 0 3 6 9 12
print(A)  # Generator still exists.
>>> <generator object <genexpr> at 0x10c63a518>
for num in A:  # Generator is exhausted as we already looped through it, won't print anything.
    print(num, end=" ")
>>>
# Nothing will be printed to terminal.


# Can also create generators by using the yield keyword.
A = [0, 3, 6, 9, 12]

def even_number_generator(arr):
    for value in arr:
        if value % 2 == 0:
            yield value

for number in even_number_generator(A):
    print("%s is even" % number)
>>> 0 is even
>>> 6 is even
>>> 12 is even

```

Note that generators do not support slicing and can't be added to a list. They can only be iterated over once. You can turn a generator into a list by using `list(my_generator)`.
