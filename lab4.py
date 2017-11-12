class Animal (object):
	def __init__(self,sound,name,age,favorite_color,food):
		self.sound = sound
		self.name = name
		self.age = age
		self.favorite_color = favorite_color
		self.food = food
	def eat(self):
		print("yummy!!" + self.name + " is eating " + self.food)
	def description(self):
		print(self.name + " is " + self.age + " years old and loves the color " + self.favorite_color)
	def make_sound(self,number):
		print((self.sound+" ") * number)
dog = Animal("waff","dog","10","brown","bones")
dog.description()
dog.eat()
dog.make_sound(7)


