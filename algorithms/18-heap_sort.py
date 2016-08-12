from heap import Heap

def heap_sort(L):
	heap = Heap()
	new = []
	for item in L:
		heap.add(item)
	for item in L:
		new.append(heap.get_max())
	return new