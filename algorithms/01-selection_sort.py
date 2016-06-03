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