class Value:
    def __init__(self, data):
        self.data = data

    def __repr__(self):
        print(f"Value(data={self.data})")

a = Value(2.0)
b = Value(2.0)
print(a.data == b.data)
print(a == b)

print(a is b)
print(id(a), id(b))

class Point:
	def __init__(self, x, y):
		self.x = x
		self.y = y
	
	def __repr__(self):
		return f"Point({self.x}, {self.y})"
	
	def dist(self):
		return (self.x**2 + self.y**2)**(1/2)

a = Point(5, 10)
