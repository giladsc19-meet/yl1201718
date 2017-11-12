class person(object):
	def __init__(self,name,fam_name,gender,age,city,street,adress,hobby):
		self.name = name
		self.fam_name = fam_name
		self.gender = gender
		self.age = age
		self.city = city
		self.street = street
		self.adress = adress
		self.hobby = hobby
	def favorite_breakfast(self,food):
		print(self.name + " likes eating " + food + " in his breakfast")
	def favorite_sport(self,sport):
		print(self.name + " likes the most " + sport + ". he considers it as his favorite sport")
	def description(self):
		print(self.name + self.fam_name + " is a " + self.gender + ". he is " + self.age + " years old. he lives in " + self.city + self.street + self.adress + ". his favorite hobby is " +  self.hobby)
p1 = person("oded"," schurr","male"," 20"," Mevaseret Zion"," Mitzpe Habira"," 70","Traveling")

p1.description()
p1.favorite_sport("doing notihng")
p1.favorite_breakfast("ice cream and coffe")