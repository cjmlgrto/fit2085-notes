class Dictionary:

	def __init__(self, table_size, prime):
		self.prime = prime
		self.item_count = 0
		self.table_size = table_size
		self.array = [None] * table_size

	def hash(self, key):
		index = 0
		a = 2692
		b = 8523
		for i in range(len(key)):
			index = (a * index + ord(key[i])) % self.table_size
			a = a * b % (self.table_size-1)
		return index

	def is_full(self):
		return self.item_count >= self.table_size

	def insert(self, key, value):
		index = self.hash(key)
		if self.is_full():
			found = False
			end = (index - 1) % self.table_size
			while index != end:
				if self.array[index][0] == key:
					self.array[index] = [key, value]
					found = True
					break
				index = (index + 1) % self.table_size
			if not found:
				raise Exception("Dictionary is full!")
		else: 
			while not self.is_full():
				if self.array[index] != None and self.array[index][0] == key:
					self.array[index] = [key, value]
					break
				if self.array[index] == None:
					self.array[index] = [key, value]
					self.item_count += 1
					break
				index = (index + 1) % self.table_size

	def search(self, key):
		index = self.hash(key)

		if self.array[index][0] == key:
			return self.array[index][1]
		else:
			end = (index - 1) % self.table_size
			if self.array[end][0] == key:
				return self.array[end][1]
			index = (index + 1) % self.table_size
			while index != end:
				if self.array[index][0] == key:
					return self.array[index][1]
				else:
					index = (index + 1) % self.table_size
			raise KeyError(str(key) + " not found!")