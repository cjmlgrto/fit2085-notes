[← Return to Index](https://github.com/cjmlgrto/fit2085-notes/)

# Searching

## Linear Search
|             | Complexity              | Note | 
|---          |---                      |---   |
| Worst Case: | **O(n)**    | Occurs when the item isn't in the list |
| Best Case:  | **O(1)**    | If the list is already sorted |

1. Check every item in the list
2. For every item, check if it is equal to the query
3. If the query is found, return True (or the index of the item)
4. If the list is sorted, and the current item is greater than the query, return False
5. If the entire list has been iterated over, return False

```python
def linear_search(L, query):
    for item in L:
        if item == query:
            return True
            
        # only for sorted lists:
        if item > query:
            return False
            
    return False
```

## Binary Search
|             | Complexity              | Note | 
|---          |---                      |---   |
| Worst Case: | **O(logn)**    | Occurs when the item isn't in the list |
| Best Case:  | **O(1)**    | If the middle item is the query |

### Assumptions:
- The list is already sorted
- The list allows random access

1. Look at the middle of the list
2. If the middle item equals the query, return True (or the index)
3. If the query is less than the middle item, _ignore_ all items after the middle item
4. Otherwise, if the query is greater the the middle item, _ignore_ all items before the middle item
5. You now have a sub-list, goto 1 and repeat until item is found.
6. If not found, return False (or -1).

```python
def binary_search(L, query):
    lower = 0
    upper = len(L) - 1
    while lower <= upper:
        mid = (lower + upper) // 2
        if L[mid] == query:
            return mid
        elif L[mid] < query:
            upper = mid - 1
        else:
            lower = mid + 1
    return -1
```


## `.index()`
A class method for lists to search for an item in the list, then return its index.

1. Use one of the search methods above
2. If not found, throw an exception
3. If there are multiple copies and the list is sorted, iterate over entire list until the first appearance of the query is found
4. Return the index of this initial appearance

```python
def index(L, query):
    position = binary_search(L, query)
    if position == -1:
        raise Exception("Item not in list!")
    
    # check for multiple copies (only for sorted lists)
    while position >= 0 and L[position] == query:
        position -= 1
    position += 1
    
    return position
```



 