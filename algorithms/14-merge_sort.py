def merge_sort(L):
    if len(L) < 2:
        return L
    else:
        mid = len(L) // 2
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
