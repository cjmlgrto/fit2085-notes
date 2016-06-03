def factorial(n):
    if n == 0: # base case
        return 1
    else:
        return n * factorial(n - 1) # recursive call

def factorial_2(n):
    return factorial_aux(n,1):

def factorial_aux(n, result):
    if n == 0:
        return result
    else:
        return factorial_aux(n-1, result*n)

def fib(n):
    if n == 0 or n == 1:
        return n
    else:
        return fib(n-2) + fib(n-1)

def fib_2(n):
    return fib_aux(n, 0, 1)

def fib_aux(n, before_last, last):
    if n == 0:
        return before_last
    else:
        return fix_aux(n-1, last, before_last+last)

def power(x, n):
    value = 1
    if n > 0:
        value = power(x, n//2)
        if n % 2 == 0:
            value = value * value
        else:
            value = value * value * x
    return value