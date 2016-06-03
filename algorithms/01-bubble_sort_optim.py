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