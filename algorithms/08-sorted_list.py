class SortedList:
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
        # if the list is empty, just insert
        if self.is_empty():
            self.the_array[self.count] = new_item
            self.count += 1
            return True

        # if it is not empty, find the correct position
        has_space_left = not self.is_full()
        if has_space_left:
            index = 0
            while index < self.count and new_item > self.the_array[index]
                index += 1

            # shift all items after indexx
            for i in range(self.count-1, index-1, -1):
                self.the_array[i + 1] = self.the_array[i]

            # insert item
            self.the_array[index] = new_item
            self.count += 1
        return has_space_left   