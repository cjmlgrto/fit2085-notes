[← Return to Index](https://github.com/cjmlgrto/fit2085-notes/)

# Complexity

## Big O Notation

- $ g(n) $ is said to be $ O(f(n)) $ if there exists constants $ K $ and $ L $ such that:

	- $ \large g(n) < Kf(n) \text{ for all } \large n > L $

- Big O Notation assumes that the actual function for runtime can be generalised to a simple function after some constant $ L $.
- For example, a program with actual runtime $ 3n^{2} + 4n $ can be generalised to $ O(n^{2}) $.

## Complexities

| Class | Big O | Example |
|---    |---    |---      |
| Constant | $O(1)$ | Adding two numbers |
| Logarithmic | $O(\log n)$ | Binary Search | 
| Linear | $O(n)$ | Linear Search |
| Super-linear | $O(n \log n)$ | Merge Sort |
| Quadratic | $O(n^{2})$ | Selection Sort |
| Exponential | $O(2^{n})$ | Brute force for $n$ items |
| Factorial | $O(n!)$ | Generating permutations of $n$ items |


