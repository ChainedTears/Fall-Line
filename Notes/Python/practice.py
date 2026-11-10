class Value:
    def __init__(self, data):
        self.data = data

    def __repr__(self):
        print(f"Value(data={self.data})")

a = Value(2.0)
b = Value(2.0)
# print(a.data == b.data)
# print(a == b)

# print(a is b)
# print(id(a), id(b))

class Point:
	def __init__(self, x, y):
		self.x = x
		self.y = y
	
	def __repr__(self):
		return f"Point({self.x}, {self.y})"
	
	def dist(self):
		return (self.x**2 + self.y**2)**(1/2)

class BankAccount:
	def __init__(self, owner, money):
		self.owner = owner
		self.money = money
	def deposit(self, money):
		self.money += money
	def withdraw(self, money):
		if (self.money - money) >= 0:
			self.money -= money 
			return True
		else:
			return False
	def balance(self):
		return self.money
	def __repr__(self):
		return f'BankAccount(owner={self.owner}, balance={self.money})'

acct = BankAccount("Arthur", 100)
acct.deposit(50)
acct.withdraw(30)
print(acct.balance())   # 120
print(acct)                  # displays: BankAccount(owner=Arthur, balance=120)
acct.withdraw(500)    # should NOT go negative; balance stays 120

class Vector():
	def __init__(self, x, y):
		self.x = x
		self.y = y
	def __repr__(self):
		return f'Vector{self.x, self.y}'
	def __add__(self, other):
		return Vector(self.x + other.x, self.y + other.y)
	def __eq__(self, other):
		return self.x == other.x and self.y == other.y
	def scale(self, scale):
		return Vector(self.x * scale, self.y * scale)
		

	
v = Vector(1, 2)
w = Vector(3, 4)

print(v)            # Vector(1, 2)
print(v + w)        # Vector(4, 6)
print(v.scale(10))  # Vector(10, 20)
print(v)            # Vector(1, 2)   <- v is unchanged!
print(v == Vector(1, 2))   # True
print(v == w)              # False