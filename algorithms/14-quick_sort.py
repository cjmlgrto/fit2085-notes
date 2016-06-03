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