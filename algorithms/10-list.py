from node import Node

class List:
   def __init__(self):
       self.head = None
       self.count = 0

   def is_empty(self):
       return self.count == 0

   def reset(self):
       self.__init__()

   def __len__(self):
       return self.count

   def _get_node(self, index):
       if index < 0 or index > self.count:
           raise Exception("Index out of bounds!")
       node = self.head
       for _ in range(index):
           node = node.next
       return node

   def insert(self, index, item):
       index = index % len(self)
       if index == 0:
           self.head = Node(item, self.head)
       else:
           node = self._get_node(index-1)
           node.next = Node(item, node.next)
       self.count += 1

   def delete(self, index):
       if self.is_empty():
           raise IndexError("The list is empty!")
       if index < 0 or index >= len(self):
           raise IndexError("Index is out of range!")
       if index == 0:
           self.head = self.head.next
       else:
          node = self._get_node(index-1)
          node.next = node.next.next
       self.count -= 1