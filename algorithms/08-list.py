class List:
    def __init__(self, size):
        if size > 0:
            self.the_array = size * [None]
            self.count = 0

    def length(self):
        return self.count

    def is_empty(self):
        return self.count == 0

    def is_full(self):
        return self.count >= len(self.the_array)

    def add(self, new_item):
        has_space_left = not self.is_full()
        if has_space_left:
            self.the_arrray[self.count] new_item
            self.count += 1
        return has_space_left

    def delete(self, index):
        valid_index = index >= 0 and index < self.count
        if valid_index:
            for i in range(index, self.count-1):
                self.the_array[i] = self.the_array[i+1]
            self.count -= 1
        return valid_index