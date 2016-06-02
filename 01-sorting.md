[← Return to Index](https://github.com/cjmlgrto/fit2085-notes/)

# Sorting

## Bubble Sort (Original)
|             | Complexity              | Note | 
|---          |---                      |---   |
| Worst Case: | **O(n<sup>2</sup>)**    | Because it has to iterate over the list for every item |
| Best Case:  | **O(n<sup>2</sup>)**    | Because it has to iterate over the list for every item
| Stability:  | **Stable**              |

1. Go through the list n times
2. For every iteration, check every adjacent pair and swap the elements if they aren't in the right order
3. For every iteration, 'lock' in the last item
4. Repeat until all items are locked

```python
def bubble_sort(L):
	 n = len(L)
	 for i in range(n - 1):
	 	 for j in range(n - 1):
	 	 	 if L[j] > L[j + 1]:
	 	 	 	L[i], L[j] = L[j], L[i]
```

## Bubble Sort (Optimised)
|             | Complexity              | Note |  
|---          |---                      |---   |
| Worst Case: | **O(n<sup>2</sup>)**    | Because it has to iterate over the list for every item |
| Best Case:  | **O(n)**                | When the list is already sorted, no swaps occur |
| Stability:  | **Stable**              |

Like the original Bubble Sort, but stop when the list is sorted.

```python
def bubble_sort_optim(L):
	 no_swaps = True
	 n = len(L)
	 for mark in range(n-1, 0, -1):
	 	 for i in range(mark):
	 	 	 if L[i] > L[i+1]:
	 	 	 	 no_swaps = False
	 	 	 	 L[i], L[i + 1] = L[i + 1], L[i]
	 	 if no_swaps:
	 	 	 break
	 	 no_swaps = True
```

## Selection Sort
|             | Complexity              | Note |
|---          |---                      |---   |
| Worst Case: | **O(n<sup>2</sup>)**    | Because it has to compare every item in the list |
| Best Case:  | **O(n<sup>2</sup>)**    | Because it has to compare every item in the list
| Stability:  | **No**              |

1. For every item in the list, find the minimum item
2. Swap the minimum item with the current selected item
3. Repeat until all items have been iterated over

```python
def selection_sort(L):
	 n = len(L)
	 for k in range(n - 1):
	 	 min = find_min(L, k)
	 	 L[k], L[min], L[min], L[k]
	 	 
def find_min(L, k):
	 min = k
	 n = len(L)
	 for i in range(k + 1, n):
	 	 if L[i] < L[min]:
	 	 	 min = i
	 return min
```

## Insertion Sort
|             | Complexity              | Note |  
|---          |---                      |---   |
| Worst Case: | **O(n<sup>2</sup>)**    | When the list is sorted in reverse |
| Best Case:  | **O(n)**                | When the list is already sorted |
| Stability:  | **Stable**              |

For every item in the list, insert it in the right position

```python
def insertion_sort(L):
	 n = len(L)
	 for mark in range(1, n):
	 	  temp = L[mark]
	 	  i = mark - 1
	 	  while i >= 0 and L[i] > temp:
	 	  	  L[i + 1] = L[i]
	 	  	  i -= 1
	 	  L[i + 1] = temp
```

	 	  
