class Heap:
    def __init__(self):
        self.count = 0
        self.array = [None]

    def __len__(self):
        return self.count

    # best case: O(1), when item is smaller or equal to parent
    # worst case: O(logN), when item has to rise all the way to the top
    def add(self, item):
        if self.count + 1 < len(self.array):
            self.array[self.count+1] = item
        else:
            self.array.append(item)
        self.count += 1
        self.rise(self.count)

    def rise(self, k):
        while k > 1 and self.array[k] > self.array[k//2]:
            self.swap(k, k//2)
            k //= 2

    def swap(self, i, j):
        self.array[i], self.array[j] = self.array[j], self.array[i]

    # best case: O(1), when item is larger or equal to largest children
    # worst case: O(log N), when the item sinks all the way to the bottom
    def get_max(self):
        assert self.count > 0, "Heap is empty!"
        maximum = self.array[0]
        self.swap(0, self.count)
        self.sink(0)
        return maximum

    def sink(self, k):
        while 2*k <= self.count:
            child = self.largest_child(k)
            if self.array[k] >= self.array[child]:
                break
            self.swap(child, k)
            k = child

    def largest_child(self, k):
        if 2*k == self.count or self.array[2*k] > self.array[2*k+1]:
            return 2*k
        else:
            return 2*k + 1