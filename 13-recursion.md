[← Return to Index](https://github.com/cjmlgrto/fit2085-notes/)

# Recursion

## Recursive Algorithms
- Solving a large problem by solving smaller sub-problems
- Each sub-problem is solved by _the same algorithm_
- Until the sub-problem is so "simple" that a trivial answer can be returned (called the **base case**)
- This is then combined and computed to solve the large problem

The general structure in Python:

```python
def solve(problem):
    if answer is simple:
        return solution
    else:
        subproblem = breakdown(problem)
        answer += solve(subproblem)
        return answer
```

### Example: Factorial
```python
def factorial(n):
    if n == 0: # base case
        return 1
    else:
        return n * factorial(n - 1) # recursive call
```

## Auxiliary Methods
- Functions can be implemented recursively
- When implemented recursively, the function may have to accept more arguments (such as passing down current answers, subproblems, etc)
- But sometimes, the functions have to be simple enough to act as an interface
- So **auxiliary** methods are used!

### Example: Node-based recursion in Linked Lists

In the Linked List class, `__contains(query)__` can be implemented recursively:

```python
def __contains__(self, item):
    # the interface sets up the auxiliary method with the recurive paramters
    return self._contains_aux(self.head, item)
    
def _contains_aux(self, current, item):
	# the auxiliary method is where the real recursion happens
    if current is None:
        return False
    return current.item == item or self._contains_aux(current.next, item)
```
### Example: Copying Linked Lists

Here is the iterative approach. Notice that the complexity is O(n<sup>2</sup>):

```python
def copy(self):
    for item in self:
        new_list.insert(len(new_list), item)
    return new_list
```

Here is the **recursive** approach, with complexity O(n):

```python
def copy(self):
    new_list = List()
    self._copy_aux(self.head, new_list)
    return new_list
    
def _copy_aux(self, node, new_list):
    if node is not None:
        self._copy_aux(node.next, new_list)
        new_list.insert(0, node.item)
```

## Terminology
- Unary: a single recursive call
- Binary: two recursive calls
- n-ary: n recursive calls
- Direct recursion: recursive calls are calls to the same function
- Indirect recursion: recursion through two or more methods (.e.g method _p_ calls method _h_ which in turn calls _p_)
- Tail recursion: where the result of the recursive call is the result of the function— that is, nothing is done in the 'way back'. Apparently closest to iteration and useulf for compilter optimisation.

### Example: Tail-recursive Factorial with Auxiliary Methods
```python
def factorial(n):
    return factorial_aux(n,1):
    
def factorial_aux(n, result):
    if n == 0:
        return result
    else:
        return factorial_aux(n-1, result*n)
```

### Example: Tail-recursive Binary Fibonacci
```python
def fib(n):
    if n == 0 or n == 1:
        return n
    else:
        return fib(n-2) + fib(n-1)
```

Notice that in this implementation, complexity is O(2<sup>n</sup>). This is because it is repeating the same computations over and over— that is, some results in either recursive call overlap.

Here's one way to fix this to achieve O(n) complexity:

```python
def fib(n):
    return fib_aux(n, 0, 1)

def fib_aux(n, before_last, last):
    if n == 0:
        return before_last
    else:
        return fix_aux(n-1, last, before_last+last)
```

### Example: Power
```python
def power(x, n):
    value = 1
    if n > 0:
        value = power(x, n//2)
        if n % 2 == 0:
            value = value * value
        else:
            value = value * value * x
    return value
```

### Example: Power using the Stack
```python
def power(x, n):
    the_stack = Stack()
    while n > 0:
        the_stack.push(n)
        n = n//2
    value = 1
    while not the_stack.is_empty():
        if the_stack.pop() % 2 == 0:
            value = value * value
        else:
            value = value * value * x
    return value
```

## Pros and Cons of Recursion

### Pros
- More natural
- Easier to prove correct
- Easier to analyse (trace a recursive call using a stack diagram)

### Cons
- Run-time overhead depending on the quality of the compiler
- Memory overhead (fewer local variables versus stack space for function call)