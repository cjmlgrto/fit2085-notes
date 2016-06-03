class Stack:
    # complexity of creating an array is O(N)
    def __init__(self, size):
        assert size > 0, "Size should be positive!"
        self.the_array = size * [None]
        self.count = 0
        self.top = -1

    # complexity is O(1) for all these methods

    def size(self):
        return self.count

    def is_empty(self):
        return self.size() == 0

    def is_full(self):
        return self.size() >= len(self.the_array)

    def push(self, new_item):
        if self.is_full():
            raise Exception("The stack is full!")
        self.top += 1
        self.the_array[self.top] = new_item
        self.count += 1

    def pop(self):
        if self.is_empty():
            raise Exception("The stack is empty!")
        item = self.the_array[self.top]
        self.top -= 1
        self.count -= 1
        return item

    def peek(self):
        if self.is_empty():
            raise Exception("The stack is empty!")
        item = self.the_array[self.top]
        return item