[← Return to Index](https://github.com/cjmlgrto/fit2085-notes/)

# MIPS Functions and Stack

## The Stack
- When writing more complex programs in MIPS, it isn't efficient to store all the variables of every function as a global variable
- Instead, functions and nested functions take advantage of the **Stack** in the memory when using _local variables_
- The stack is literally just a stack of variables in which newly-allocated variables are piled on top, then removed when finished
- The stack is useful for nesting functions or even recursive functions, where a lot of _local variables_ are necessary

| Example Stack Diagram | Addresses |
|:--:           | :--- |
|  ...           | Lower addresses ↑  |
| `5`   | `0x7FFF310C` |
| `4`   | `0x7FFF3110` |
| `29`  | `0x7FFF3114` |
| ... | Higher addresses ↓ |

- A register called the _stack pointer_ stores the address of the top of the stack. In the example above, the stack pointer, `$sp`, contains the address `0x7FFF310C`, in which the integer `5` 'lives'.
- The _stack pointer_ **always** points to the top of the stack.
- There is another register called the _frame pointer_. This register is often used as the 'base' pointer of a new 'sub stack'. Functions use this to reference arguments and variables that were allocated before the function was called. (Because it can get out of hand to try and get the relative position of arguments as the stack pointer keeps growing).

## Function Conventions

### Calling Functions
1. Save temporary registers onto stack
2. Pass arguments onto stack
3. Call function with `jal`
4. Callee saves `$ra`
5. Callee saves `$fp`
6. Copy `$sp` to `$fp`
7. Allocate local variables to stack

```assembly
main:		
			# reset stack frame
			addi 	$fp, $sp, 0
			
			# move stack pointer for n local variables
			addi 	$sp, $sp, -4n

			# store local variables using frame pointer
			sw 		$0, -4n($fp)
			# ...
			sw		$0, -4($fp)

			# move stack pointer up for k
			addi	$sp, $sp, -4k

			# push arguments using stack pointer
			sw		$0, [4k-4]($sp)
			# ...
			sw 		$0, 0($sp)

			# call function
			j 		function

			# ...

function:
			# move stack pointer for ra and fp
			addi	$sp, $sp, -8

			# push fp then ra
			sw		$fp, 0($sp)
			sw		$ra, 4($sp)

			# reset stack frame
			addi	$fp, $sp, 0

			# move stack pointer for j local variables
			addi 	$sp, $sp, -4j

			# store local variables using frame pointer
			sw 		$0, -4j($fp)
			# ...
			sw		$0, -4($fp)

			# ...

			# to access the arguments, use frame pointer positive offset + 8
			lw		$t0, [4k + 8]($fp)

			# to access local variables, use frame pointer negative offset
			lw		$t1, -4j($fp)

			# ...

			# store return value in v0
			add		$v0, $t0, $1

			# move stack pointer down to pop local variables
			addi	$sp, $sp, 4j

			# copy ra then fp
			lw		$ra, 4($fp)
			lw		$fp, ($fp)

			# move stack pointer down
			addi	$sp, $sp, 4

			# return back to function caller
			jr  	$ra
```

By the end of this, `$fp` must be pointing to the 'bottom' of your new 'sub-stack' (and **must contain** the previous value of `$fp`), and your stack should look like this:

| Function Stack Diagram |
|:--:           |
|  ...           |
| $fp   |
| $ra   |
| argument `a`  |
| argument `b` |
| argument `c` |
| `some var` |
| ... |

### Finishing Functions
1. Store return value into `$v0`
2. Remove all local variables off the stack
3. Decrement `$sp` accordingly
4. Reload `$fp` then `$ra`
5. Decrement `$sp`
6. Jump back

```assembly
			# copy return value into $v0
			addi	$v0, $blah, 0
			
			# remove local variables
			# decrement by n local variables * 4
			addi	$sp, $sp, 4n
	
			# re-assigned $fp and $ra
			lw		$fp, 0($sp)
			lw		$ra, 4($sp)
			addi	$sp, $sp, 8
	
			jr		$ra

