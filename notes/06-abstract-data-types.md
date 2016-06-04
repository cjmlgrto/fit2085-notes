[← Return to Index](https://github.com/cjmlgrto/fit2085-notes/)

# Abstract Data Types

## Data Types
- A data type combines data storage with a set of operations to interact with data

## Abstract Data Types
- Are data structures with their own operations— or known as an _interface_ (e.g. lists have `len()` or `append()`)
- They can also be referred to as _objects_.
- An abstract data types hides its implementation from the user, so the user's code is independent from its implementation and the user does not have to know how it is implemented.

### Abstraction
- Extracting essential information while ignoring the rest
- Making things simpler, so you don't have to know how it works
- For example, you can just type `print()` instead of having to figure out how the computer does it all manually

### Encapsulation
- Enclosing items within a container
- For example, loops have their own statements, or modules have their own local variables

### Information Hiding
- Blocking access to information
- For example, a function that decrypts a password into a variable— the variable shouldn't be visible to any other function but itself

### Data Types
- Variables can be assigned values— and these values can be of any _data type_.
- For example, integers or booleans

### Data Structures
- Complex structures of data types
- For example, tables, lists, or even dictionaries

One example of an Abstract Data Type could be a _Sudoku Puzzle_. The underlying data structure would be a table— made up of lists— which are also made up of integers. The interface could involve `print()`, `insert()` or even `check()` to see if it has been solved.

What's great about Abstract Data Types is that you don't often need to know how they're implemented— you just have to know how to use the interface.

### Fundamental Abstract Data Types
- **Containers** (stores and removes items independent of contents)
- **Dictionaries** (permits access to data via a key)
- **Priority Queue** (accesses items in a specific order)

