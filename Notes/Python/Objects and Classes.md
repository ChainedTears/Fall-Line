## Objects
In python, everything is an object. This includes, and is not limited to,

```python
2.0, [1, 2, 3], "hello"
```

An object is a bundle of data and the operations that can handle that data, stored together in memory. An object would usually contain:
- The **data**, called *attributes* (For example, the characters in a string or numbers in a list)
- The **behaviour**, called *methods*, which are functions attached to the object (For example, `.append()` for lists or `.upper()` on a string)
- The **type**, which says what kind of object it is
## Classes
A class is a **type**. It is the definition of the data the object can hold and methods that can be used to manipulate that data. 

When you run

```python
class Value:
	def __init__(self, data):
		self.data = data
	
	def __repr__(self):
		return f"Value(data={self.data})"
```

, python builds a new class named `Value`, then it reads each ``def`` and stores it on the class as a ``method``. `Value` now refers to the name of that newly built class. Nothing will be printed, and no objects currently exists.

The method runs later, when you add

```python
a = Value(2.0)
```

When executed, python will create a new `Value` object. Then `__init__(that_object, 2.0)` will run. Inside the function, the original `self` parameter is the new object and data is `2.0`. ``self.data`` attaches `2.0` to the new object as its `data` attribute. When `__init__` finishes, the local `data` is deleted, and the finished object is assigned to the variable `a`.

Later, when `a` is written, Python calls 

```python
a.__repr__()
```

which builds the string 

```python
f"Value(data={self.data})"
```

## Practice

```python
# Make a class `Point` that stores an `x` and a `y`. Give it a `__repr__` so that `Point(3, 4)` displays as `Point(3, 4)`. Then add a normal method called `dist()` that returns the distance from the origin, so `Point(3, 4).dist()` gives `5.0`.

class Point:
	def __init__(self, x, y):
		self.x = x
		self.y = y
	
	def __repr__(self):
		return f"Point({self.x}, {self.y})"
	
	def dist(self):
		return (self.x**2 + self.y**2)**(1/2)

```