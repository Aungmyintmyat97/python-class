#class Person:
#	pass

#p = Person()
#print(p)

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
#
# 	def say_hi(self):
# 		print('Hello, my name is ', self.name)
#
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

class Dog:
	"""Represent a dog, with a name"""

	population = 0

	def __init__(self,name):
		"""calling the data"""

		self.name = name
		print("(calling{}".format(self.name))

		Dog.population += 1

	def go(self):
		"""I am going away."""

		print("{} is going away!".format(self.name))

		Dog.population -= 1

		if Dog.population == 0:
			print("{} was the last one.".format(self.name))
		else:
			print("They are still {:d} eating".format(self.name))

	def feeding(self):
		"""Feeding the dog."""

		print("feeding the food to {} by me.".format(self.name))

	@classmethod
	def how_many(cls):
		print("There are {:d} dogs.".format(cls.population))

droid1 = Dog(" Gote Kyar")
droid1.feeding()
Dog.how_many()

droid2 = Dog(" Bo Phyu")
droid2.feeding()
Dog.how_many()

droid3 = Dog(" Aung Nat")
droid3.feeding()
Dog.how_many()

print("\n Dog are eating food.\n")

print("Dog have done eating food. So let's them go")
droid1.go()
droid2.go()
droid3.go()

Dog.how_many()
