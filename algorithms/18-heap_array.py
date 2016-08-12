class Heap:
    def __init__(self):
        self.count = 0
        self.array = [None]

    def __len__(self):
        return self.count

    def __str__(self):
        return str(self.array)

    def add(self, item):
        self.array.append(item)
        self.count += 1
        self.rise(self.count)

    def rise(self, k):
        while self.array[k] > self.array[k//2] and k > 1:
            self.swap(k, k//2)
            k //= 2

    def swap(self, i, j):
        self.array[i], self.array[j] = self.array[j], self.array[i]

    def get_max(self):
        self.swap(1, self.count)
        maximum = self.array.pop(self.count)
        self.count -= 1
        self.sink(1)
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