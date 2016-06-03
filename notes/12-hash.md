[← Return to Index](https://github.com/cjmlgrto/fit2085-notes/)

# Hash Tables

## Dictionaries

```python
english_german = {
    'monday':'montag', 
    'tuesday':'dienstag',
    'wednesday':'mittwoch',
    'thursday':'donnerstag',
    'friday':'freitag',
    'saturday':'samstag',
    'sunday':'sonntag'
}

car = {
    'color':'red',
    'seats': 4, 
    'brand':'Tesla'
}

students = {
	'26928555':'Roberto',
	'26829814':'Pablo',
	'28590767':'Patricia'
}
```
- A dictionary is a list of _key-value_ pairs.
- Every value has a corresponding key, and can only be retrieved using its key.
- Operations are: search, insert and delete.
- Implemented using **hash tables**.

## Hash Tables

### Data
- Each item must have a unique key— or the value is converted into a unique key through _hashing_.
- Underlying data structure is either an incredibly large array or a linked list

### Operations
- Hash (maps a unique key to a position in the list)
- Insert
- Search
- Delete

### Hashing
Converts a specified word into a unique key that can be used to determine its position in the underlying array.

The goal is to have a function that maps a _unique_ key for any input value— this is to ensure no 'collisions' occur (that is, two differnt words having the same key).

Below is a _universal_ hash function implemented in Python. It is best to use prime numbers for `TABLE_SIZE`, `a` and `b`.

```python
def hash_function(word, TABLE_SIZE):
    value = 0
    # random seeds
    a = 10651
    b = 10531
    for i in range(len(word)):
        value = (a*value + ord(word[i])) % TABLE_SIZE
        a = a * b % (TABLE_SIZE-1)
    return value
```

### Insertion
1. Use the hash function to get a position
2. Try to insert at position
3. Otherwise, deal with the collision

### Search ("Check if in hash table")
1. Use hash function to get a position
2. If the query matches, return True
3. Otherwise, deal with the collision until found
4. If not found, return False

### Delete
1. Use the hash function to get a position
2. Search for the item, deal with collisions
3. If it exists and is found, remove the item

## Collision Resolution ("Open Addressing")

### Linear Probing
- Checking every item in the array until the position's conditions are perfect
- Check query position, then look at the next, then the next... wrapping around the entire table until you're back to the original position

### Quadratic Probing
- Like Linear Probing, but moving in larger and larger steps, wrapping around the list
- A problem with probing is that items with similar hash values tend to 'cluster'

### Double Hashing
- Using a second hash function to determine the probe 'step' to prevent clustering
- Should not hash to 0, and the table size and step size are co-prime

### Seperate Chaining
- Using linked lists for every item in the large array
- If a collision occurs, just append a node to the end of the chain in the array position and traverse


## Example: Hash Table Dictionary Object
```python
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
```