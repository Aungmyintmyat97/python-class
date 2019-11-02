# class Person:
# 	pass
#
# p = Person()
# print(p)

#Methods

# class Person:
# 	def say_hi(self):
# 		print('Hello, how are you>')
#
# p = Person()
# p.say_hi()

#__init___method

# class Person:
# 	def __init__(self,name):
# 		self.name = name

# 	def say_hi(self):
# 		print('Hello, my name is ', self.name)

# p = Person('Aung_Myint_Myat')
# p.say_hi()


# class Dog:
# 	def __init__(self,name):
# 		self.name = name
#
# def say_hi(self):
# 	print('hello, I am ', self.name)
#
# d = Dog('the dog')
# d.say_hi()
#
# dog = dog('Name')
# dog.color('black')
# dog.owner('Aung')
#
# dog.function() - bark
# 			- eat
# 			- sleep
# 			- bite

#Class and Object variables


# class Robot:
# 	"""Represent a robot, with a name."""
#
# 	population = 0
#
# 	def __init__(self,name):
# 		"""Initializes the data."""
#
# 		self.name = name
# 		print("(Initializing{})".format(self.name))
#
# 		Robot.population += 1
#
# 	def die(self):
# 		"""I am dying."""
#
# 		print("{} is being destroyed!".format(self.name))
#
# 		Robot.population -= 1
#
# 		if Robot.population == 0:
# 			print("{} was the last one.".format(self.name))
# 		else:
# 			print("There are still {:d} robots working.".format(Robot.population))
#
# 	def say_hi(self):
# 		"""Greeting by the robot.
#
# 		Yeah, they can do that."""
#
# 		print("Greetings, my sister call me{}.".format(self.name))
#
# 	@classmethod
# 	def how_many(cls):
# 		"""Prints the current population."""
# 		print("We have {:d} robots.".format(cls.population))
#
# droid1 = Robot(" R2-D2")
# droid1.say_hi()
# Robot.how_many()
#
# droid2 = Robot(" C-3PO")
# droid2.say_hi()
# Robot.how_many()
#
# droid3 = Robot(" Q-35")
# droid3.say_hi()
# Robot.how_many()
#
# print("\nRobots can do some work here.\n")
#
# print("Robots have finished their work. so let's destroy them")
# droid1.die()
# droid2.die()
# droid3.die()
#
# Robot.how_many()

# class Dog:
# 	"""Represent a dog, with a name."""

# 	population = 0

# 	def __init__(self,name):
# 		"""calling the data."""

# 		self.name = name
# 		print("(calling{})".format(self.name))

# 		Dog.population += 1

# 	def go(self):
# 		"""I am going away."""

# 		print("{} is going away!".format(self.name))

# 		Dog.population -= 1

# 		if Dog.population == 0:
# 			print("{} was the last one.".format(self.name))
# 		else:
# 			print("They are still {:d} dogs eating food.".format(Dog.population))

# 	def feeding(self):
# 		"""Feeding the dog."""

# 		print("feeding the food to{} by me.".format(self.name))

# 	@classmethod
# 	def how_many(cls):
# 		"""Prints the current population."""
# 		print("There are {:d} dogs.".format(cls.population))

# droid1 = Dog(" Gote Kyar")
# droid1.feeding()
# Dog.how_many()

# droid2 = Dog(" Bo Phyu")
# droid2.feeding()
# Dog.how_many()

# droid3 = Dog(" Aung Nat")
# droid3.feeding()
# Dog.how_many()

# print("\nDog are eating food.\n")

# print("Dog have done eating food. So let's them go.")
# droid1.go()
# droid2.go()
# droid3.go()

# Dog.how_many()



#inheritance

# class SchoolMember:
# 	'''Represents any school member.'''
#
# 	def __init__(self, name, age):
# 		self.name = name
# 		self.age = age
# 		print('Initialized SchoolMember: {}'.format(self.name))
#
# 	def tell(self):
# 		"""Tell my details."""
# 		print('Name:"{}" Age:"{}" '.format(self.name, self.age),end="")
#
#
# class Teacher(SchoolMember):
# 	'''Represents a student.'''
#
# 	def __init__(self, name, age, marks):
# 		SchoolMember.__init__(self, name, age)
# 		self.marks = marks
# 		print('Initialized Student: {}'.format(self.name))
#
# 	def tell(self):
# 		SchoolMember.tell(self)
# 		print('Marks: "{:d}"'.format(self.marks))
#
# class Student(SchoolMember):
# 	'''Represents a Student'''
#
# 	def __init__(self, name, age, marks):
# 		SchoolMember.__init__(self, name, age)
# 		self.marks = marks
# 		print('Initialized Student: {}'.format(self.name))
#
# 	def tell(self):
# 		SchoolMember.tell(self)
# 		print('Marks: "{:d}"'.format(self.marks))
#
# class Headmaster(SchoolMember):
# 	'''Represents a Headmaster'''
#
# 	def __init__(self, name, age, marks):
# 		SchoolMember.__init__(self, name, age)
# 		self.marks = marks
# 		print('Initialized Headmaster: {}'.format(self.name))
#
# 	def tell(self):
# 		SchoolMember.tell(self)
# 		print('Marks: "{:d}"'.format(self.marks))
#
# t = Teacher('Mrs. Shrividya', 40, 30000)
# s = Student('Swaroop', 25, 75)
# h = Headmaster('Mrs. David', 42, 25000)
#
# print()
#
# members =[t,s,h]
# for member in members:
# 	member.tell()


class Dog:

	def __init__(self, name, age, gender):
		self.name = name
		self.age = age
		self.gender = gender
		print('Initialized Dog: {}'.format(self.name))

	def bark(self):
		'''Tell details.'''
		print('Name:"{}" Age:"{}" Gender:"{}"'.format(self.name, self.age, self.gender),end="")

class Shamoyed(Dog):

	def __init__(self, name, age, gender, child):
		Dog.__init__(self, name, age, gender)
		self.child = child
		print('Dog Name:{}'.format(self.name))

	def bark(self):
		Dog.bark(self)
		print('Child: "{:d}"'.format(self.child))

class GoldenRetriver(Dog):

	def __init__(self, name, age, gender, child):
		Dog.__init__(self, name, age, gender)
		self.child = child
		print('Dog Name:{}'.format(self.name))

	def bark(self):
		Dog.bark(self)
		print('Child: "{:d}"'.format(self.child))

class Husky(Dog):

	def __init__(self, name, age, gender, child, master):
		Dog.__init__(self, name, age, gender)
		self.child = child
		self.master = master
		print('Dog Name:{}'.format(self.name))

	def bark(self):
		Dog.bark(self)
		print('Child: "{}" Master: "{:d}"'.format(self.child, self.master))

s = Shamoyed('Bo Bo', 4, 'Female', 4)
g = GoldenRetriver('Bo Phyu', 3, 'Male', 1)
h = Husky('Tiger', 6, 'Male', 2, 2)

print()

dogfamily = [s, g, h]
for dog in dogfamily:
	dog.bark()



