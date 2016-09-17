class TrieNode:
	def __init__(self, char, value=None):
		#	@author Carlos Melegrito (26928523)
		#	@since Sat Sep 10 16:38:36 2016
		#	@modified Sat Sep 10 16:38:37 2016
		#	@pre char is a single, lowercase, alphabetic character
		#	@post initialises a new node for the Trie class
		#	@complexity worst-time: O(1), worst-space: O(n^n)
		#	@param char: the character associated with the node; value: any value to be associated with the character

		#	Set node's own values
		self.char = char
		self.value = value
		#	Prepare for child nodes
		self.children = [None] * 26
		#	The following array stores the indices of none-None elements of the above array, for time efficiency
		self.indices = []

	def __contains__(self, char):
		#	@author Carlos Melegrito (26928523)
		#	@since Sat Sep 10 16:41:52 2016
		#	@modified Sat Sep 10 16:41:53 2016
		#	@pre the current node has been initalised, and char is a single, lowercase, alphabetic character
		#	@post returns True if the character is in the array of children, else false
		#	@complexity worst-time: O(1), worst-space: O(1)
		#	@param char: a queried character

		#	Check if a node exists in the array
		if self.children[ord(char) % 26] is None:
			return False
		else:
			return True

	def __setitem__(self, char, value):
		#	@author Carlos Melegrito (26928523)
		#	@since Sat Sep 10 16:43:21 2016
		#	@modified Sat Sep 10 16:43:22 2016
		#	@pre char is a single, lowercase, alphabetic character
		#	@post a shorthand function to add a new child node to the current node
		#	@complexity worst-time: O(1), worst-space: O(1)
		#	@param char: the character associated with the node; value: a new node object

		i = ord(char) % 26
		self.children[i] = value
		self.indices.append(i)

	def __getitem__(self, char):
		#	@author Carlos Melegrito (26928523)
		#	@since Sat Sep 10 16:45:11 2016
		#	@modified Sat Sep 10 16:45:12 2016
		#	@pre char is a single, lowercase, alphabetic character
		#	@post returns the node object of the associated character
		#	@complexity worst-time: O(1), worst-space: O(1)
		#	@param char: the character associated with the node

		return self.children[ord(char) % 26]

class Trie:
	def __init__(self):
		#	@author Carlos Melegrito (26928523)
		#	@since Sat Sep 10 16:46:36 2016
		#	@modified Sat Sep 10 16:46:37 2016
		#	@pre none
		#	@post initialises a new empty Trie
		#	@complexity worst-time: O(1), worst-space: O(1)
		#	@param none

		self.root = TrieNode('')

	def insert(self, string, value):
		#	@author Carlos Melegrito (26928523)
		#	@since Sat Sep 10 16:47:10 2016
		#	@modified Sat Sep 10 16:47:11 2016
		#	@pre string is a string containing only lowercase alphabetic characters, value is an object
		#	@post inserts the string and corresponding value into the Trie
		#	@complexity worst-time: O(n)
		#	@param string: the input string, value: any object to be associated with the string

		current = self.root
		for char in string:
			#	If the current character of the string is not a child of the current node,
			if char not in current:
				#	Create a new child node for the current character
				current[char] = TrieNode(char)
			#	Set the current node to this new child
			current = current[char]
		#	Once the end of the string is reached, set the current node's value to the given value
		current.value = value

	def get(self, string):
		#	@author Carlos Melegrito (26928523)
		#	@since Sat Sep 10 16:50:02 2016
		#	@modified Sat Sep 10 16:50:03 2016
		#	@pre string is a string containing only lowercase alphabetic characters 
		#	@post returns the value associated with that string, otherwise returns None
		#	@complexity worst-time: O(n)
		#	@param string: the input string

		current = self.root
		for char in string:
			#	If the current character is in the children of the current node
			if char in current:
				#	Set the new current node to the child with that character
				current = current[char]
			else:
				#	Otherwise, if it isn't in the current node, return None
				return None
		#	Once found, return the value
		return current.value

	def match(self, prefix):
		#	@author Carlos Melegrito (26928523)
		#	@since Sat Sep 10 16:51:54 2016
		#	@modified Sat Sep 10 16:51:55 2016
		#	@pre prefix is a string composed of only lowercase alphabetic characters
		#	@post returns a list of words that share the given input prefix
		#	@complexity worst-time: O(m + n), where m is the prefix and n is the number of words with the prefix
		#	@param prefix, the input string

		current = self.root
		for char in prefix:
			#	If the current character is in the children of the current node
			if char in current:
				#	Set the new current node to the child with that character
				current = current[char]
			else:
				#	Otherwise, if it isn't in the current node, return None
				return None
		#	Once found, get all the matching words
		return self.collect(current)

	def collect(self, current):
		#	@author Carlos Melegrito (26928523)
		#	@since Sat Sep 10 16:54:12 2016
		#	@modified Sat Sep 10 16:54:13 2016
		#	@pre current is a TrieNode object
		#	@post returns a list of all the words and their values within the input current node
		#	@complexity worst-time: O(m + n), where m is the prefix and n is the number of words with the prefix
		#	@param current: the node to be traversed

		collection = []
		#	Run the recursive auxiliary function
		self._collect_aux(current, collection)
		return collection

	def _collect_aux(self, current, collection):
		#	@author Carlos Melegrito (26928523)
		#	@since Sat Sep 10 16:56:02 2016
		#	@modified Sat Sep 10 16:56:03 2016
		#	@pre current is a TrieNode object, collection is an array
		#	@post appends the values of all TrieNodes with values into the collection array
		#	@complexity worst-time: O(m + n), where m is the prefix and n is the number of words with the prefix
		#	@param current: the node to be traversed, collection: the array to append values to

		#	If the current node has a value (aka, is a valid word in the dictionary)
		if current.value is not None:
			collection.append(current.value)
		for i in current.indices:
			#	Then, traverse each child node for their values, and recurse
			self._collect_aux(current.children[i], collection)