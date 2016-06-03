[← Return to Index](https://github.com/cjmlgrto/fit2085-notes/)

# Recursive Sorting

## Merge Sort

|             | Complexity              | Note | 
|---          |---                      |---   |
| Worst Case: | **O(n log n)**    | Height of the binary tree times merge complexity |
| Best Case:  | **O(n log n)**    | Height of the binary tree times merge compexity
| Stability:  | **Stable**              |

1. Split the list into two
2. For each sublist, split it again
3. Once fully split, merge back in the right order

```python
def merge_sort(L):
    if len(L) < 2:
        return L
    else:
        mid = len(array) // 2
        left = merge_sort(L[:mid])
        right = merge_sort(L[mid:])
        return merge(left, right)

def merge(L, R):
    i = 0
    j = 0
    ordered = []
    while i < len(L) and j < len(R):
        if L[i] < R[j]:
            ordered.append(L[i])
            i += 1
        elif L[i] > R[j]:
            ordered.append(R[j])
            j += 1
        else:
            ordered.append(L[i])
            i += 1
            ordered.append(R[j])
            j += 1
    while i < len(L):
        ordered.append(L[i])
        i += 1
    while j < len(R):
        ordered.append(R[j])
        j += 1
    return ordered
```

## Quicksort

|             | Complexity              | Note | 
|---          |---                      |---   |
| Worst Case: | **O(n<sup>2</sup>)**    | Height of the binary tree times merge complexity |
| Best Case:  | **O(n log n)**    | Height of the binary tree times merge compexity
| Stability:  | **No**              |

1. Partition the list
2. Sort the first part (recursively)
3. Sort the second part (recursively)

To partition:

1. Choose an item, called the pivot then put it at the front of the list
2. Create a variable called the boundary and set it to the position of the pivot
3. Iterate over every item after the pivot
4. If the item is greater than the pivot, ignore
5. If it is less than the pivot, swap it with the item next to the boundary, then increment the boundary
6. Continue until the entire list has been iterated over
7. Swap the boundary with the pivot so that the pivot is now in the 'middle' of the list
8. Do this again for every sublist before and after the pivot

```python
def quick_sort(L):
    start = 0
    end = len(L)-1
    quick_sort_aux(L, start, end)

def quick_sort_aux(L, start, end):
    if start < end:
        boundary = partition(L, start, end)
        quick_sort_aux(L, start, boundary-1)
        quick_sort_aux(L, boundary+1, end)

def partition(L, start, end):
    mid = (start + end) // 2
    pivot = L[mid]
    L[start], L[mid] = L[mid], L[start]
    index = start
    for k in range(start+1, end+1):
        if L[k] < pivot:
            index += 1
            L[k], L[index] = L[index], L[k]
    L[index], L[start] = L[start], L[index]
    return index
```
    