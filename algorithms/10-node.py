class Node:
    def __init__(self, item=None, next=None):
        self.item = item
        self.next = next

    def __str__(self):
        return str(self.item)