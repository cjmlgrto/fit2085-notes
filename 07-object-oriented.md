[← Return to Index](https://github.com/cjmlgrto/fit2085-notes/)

# Object-Oriented Programming

## Objects
- An object is a thing
- Things have *attributes* and *methods*
- Attributes are an objects' features and characteristics— for example, a car is an object, and can be red, blue, have spoilers or none
- Methods are an objects' actions— for example, a car can drive forward, backwards or even honk
- *Even a collection of objects* can be an object! For example, a 'laptop' could be a Windows computer, Chromebook, or even a Mac.
- And each individual object within an object has its own attributes and methods!
- Sometimes, the sub-objects within an object can inherit the characteristics of the parent object— for example, dogs have four legs, and a Shiba Inu can also have four legs!
- But it can't go the other way around! If your pet somehow has three legs, it doesn't mean all other dogs should have three legs.
- This same inheritance idea also applies to an object's methods
- All of this can be applied to programming— thus, this is the concept of object-oriented programming

## Variables in Python
- In Python, variables are essentially 'names' store in memory that point to another specific location in memory, which holds a value.
- For example, assigning `x = 10` means a 'chunk of memory' is created for the value `10`, and on the system memory stack, the reference `x` is created, which points to the 'chunk'— or _object_ that holds `10`.
- **You can assign values of different types to the same variable**
- **Assignments do not alter the object itself. They only alter the reference.** Then, the variable will refer to a different object.

### Mutability and Immutability
- Lists are **mutable**— they can be changed even when re-assigned

```python
L = [1,2,3]
K = L
K[0] = 5
print(K)
>>> [5,2,3]
print(L)
>>> [5,2,3]
```

- Integers are **immutable**— once re-assigned, a new object is referenced

```python
X = 5
Y = X
Y += 1
print(Y)
>>> 6
print(X)
>>> 5
```

## Namespaces and Scope
In a nutshell: every time you nest and call a new variable, it is exclusive to that nest.

```python
x = 10
def a(x):
	 return x
	 
def b():
	 return x
	 
def c():
	 x = 5
	 return x
```
In the above scenario:

- `a(x)` passes the global variable, `x` then returns 10
- `b()` returns the global variable, `x`, which is 10
- `c()` uses a **local** variable `x`, then returns 5

During execution, Python's scope searches **from the inside out**. That is, it looks for the most local variable name first, and if it does not exist, continues to search until it has to search the built-in modules for it.

## Classes
Are code implementations of objects in object-oriented programming.

### Building Classes

```python
class Car:
		wheels = 4

		def __init__(self):
			self.seats = 4
			self.color = "red"
		
		def drive(self):
			...
```
- All methods in the class must accept the variable ``self``— which refers to... itself.
- Contains the `__init__(self)` method, which occurs whenever the class is initialised.

### Using Classes
1. _Initialise_ the class by assigning it to a unique variable
2. _Qualify_ using dot syntax to access the methods and attributes of the class
3. $$$

```python
my_car = Car()
print(my_car.seats)
>>> 4
print(my_car.color)
>>> "red"

my_car.color = "blue"
print(my_car.color)
>>> "blue"

my_car.drive()
...
```
- Changing the attribute of an instance can be done by qualifying it
- Note that changing the default attributes of a class will affect all _new_ instances, for example:

```python
my_car = Car()
your_car = Car()
print(my_car.wheels)
>>> 4
print(your_car.wheels)
>>> 4

my_car.wheels = 5
print(my_car.wheels)
>>> 5
print(your_car.wheels)
>>> 4
 
Car.wheels = 10
their_car = Car()


print(my_car.wheels)
>>> 5
print(your_car.wheels)
>>> 4
print(their_car.wheels)
>>> 10
```

## Exception Handling
1. **Try** to meet a _precondition_
2. If nothing happens, proceed as normall
3. Otherwise, if an **Except**ion occurs, execute another block of code that would work without the right _precondition_

```python
try:
	...
	value = something
	...
except:
	do something else...
```




