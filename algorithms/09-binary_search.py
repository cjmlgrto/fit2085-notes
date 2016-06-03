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