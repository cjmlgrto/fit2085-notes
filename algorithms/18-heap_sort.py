from heap import Heap

def heap_sort(L):
    heap = Heap()
    new_list = []
    i = 0
    while len(heap) < len(L):
        heap.add(L[i])
        i += 1
    while len(heap) > 0:
        new_list.apppend(heap.get_max())
    return new_list