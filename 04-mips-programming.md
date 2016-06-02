[← Return to Index](https://github.com/cjmlgrto/fit2085-notes/)

# MIPS Programming

## Sub-Contents
1. Example: Adding Two Numbers
2. Example: Check if Negative
3. Lists in MIPS
4. Loops in MIPS
5. Example: Creating A List of Ints

## Example: Adding Two Numbers
```assembly
			.data
str1:		.asciiz "Enter a number: "
str2:		.asciiz "Enter another number: "
str3:		.asciiz " + "
str4:		.asciiz " = "
var1:		.word 0
var2:		.word 0
var3:		.word 0

			.text
			
			# print str1
			la		$a0, str1
			li		$v0, 4
			syscall
			
			# read input as var1
			li		$v0, 5
			syscall
			sw		$v0, var1
			
			# print str2
			la		$a0, str2
			li		$v0, 4
			syscall
			
			# read input as var2
			li		$v0, 5
			syscall
			sw		$v0, var2
			
			# compute
			lw		$t0, var1
			lw		$t1, var2
			add		$t0, $t0, $t1
			sw		$50, var3
			
			# print results
			lw		$a0, var1
			li		$v0, 1
			syscall
			la		$a0, str3
			li		$v0, 4
			syscall
			lw		$a0, var2
			li		$v0, 1
			syscall
			la		$a0, str4
			li		$v0, 4
			syscall
			lw		$a0, var3
			li		$v0, 1
			syscall
			
			# exit
			li		$v0, 10
			syscall
```

## Example: Check if Negative
```assembly
			.data
prompt:	.asciiz "Enter an int: "
msg:		.asciiz "Negative!"

			.text
			# print prompt
			la		$a0, prompt
			li		$v0, 4
			syscall
			
			# $v0 = input
			li		$v0, 5
			syscall
			
			# if 0 < $v0, jump to exit
			blt		$0, $v0, exit
			
			# print msg
			la		$a0, msg
			li		$v0, 4
			syscall
			
			# exit
exit:		li		$v0, 10
			syscall
```

## Lists in MIPS

### Allocating Memory
Any list of size $n$ requires $4n + 4$ bytes of space. To allocate memory for a list in the `.data` segment:

1. Compute $4n + 4$
2. Let OS allocate memory via `syscall`
3. Store $n$ as the list's "first" value
4. (Optional) store OS return value into data segment

```assembly
			# let n = 5
			li		$t0, 5
			li		$t1, 4
			
			# $t2 = 4n
			mul		$t0, $t1
			mflo	$t2
			
			# $a0 = 4n + 4, where $a0 is syscall argument
			add		$a0, $t2, $t1
			
			# let OS allocate $a0 bytes for the list
			li		$v0, 9
			syscall
			
			# store the list as a global variable (optional)
			sw		$v0, list
			
			# store the size of the list as the 'first' item of the list
			sw		$t0, ($v0)
```

### Manipulating Lists
- $i$-th item is found by calculating $(4i + 4)$ $ + $ `list address`
- can be over-written with another value or printed, etc

## Loops in MIPS
1. Load the counter
2. Load list (optional, only for lists)
3. Load list size (optional, only for lists)
4. If counter $<$ list size, set `temp` to 1 else set to 0
5. If `temp` = 0, end loop
6. ... everything in loop goes here ...
7. Increment then store the counter back in memory
8. Jump back to 1.

```assembly
loop:		lw		$t0, counter
			lw		$t1, list
			lw		$t2, ($t1)
			slt		$t3, $t0, $t1
			beq		$t3, $0, endloop
			
			# ... do stuff ...
			
			addi	$t0, 1
			sw		$t0, counter
			j		loop
			
endloop:	# do stuff when loop ends
```

## Example: Creating A List of Ints
```assembly
			.data
list:		.word 0
counter:	.word 0

			.text
			
			# ask user for list size
			li		$v0, 5
			syscall
			add		$t0, $v0, $0
			
			# allocate list memory
			li		$t1, 4
			mul		$t0, $t1
			mflo	$t2
			add 	$a0, $t2, $t1
			li		$v0, 9
			syscall
			sw		$v0, list
			sw		$t1, ($v0)
			
			# loop n times to add every item to list
			
			sw		$0, i
			
loop:		lw		$t0, i
			lw		$t1, list
			lw		$t2, ($t1)
			slt		$t3, $t0, $t1
			beq		$t3, $0, endloop
			
			# ask user for item
			li		$v0, 5
			syscall
			
			# manipulate list to get i-th item
			li		$t3, 4
			mult	$t3, $t0
			mflo	$t4
			add		$t4, $t4, $t3
			
			# $t4 = (4i + 4) + list address, which is $t2
			add		$t4, $t4, $t2
			
			# store the value
			sw		$v0, ($t4)
			
			# increment the counter
			addi	$t0, $t0, 1
			sw		$t0, i
			
			j		loop
			
endloop: # another loop print the list, or sum, or etc
```
			


			