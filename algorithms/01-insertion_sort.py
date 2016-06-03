def insertion_sort(L):
     n = len(L)
     for mark in range(1, n):
          temp = L[mark]
          i = mark - 1
          while i >= 0 and L[i] > temp:
              L[i + 1] = L[i]
              i -= 1
          L[i + 1] = temp