# TODO
# practice inheritance - qith character class
# 	allow us to have players and NPC's that share traits
# Add some stats generation code

class Player:
	# Init function(when an object is created)
	def __init__(self, name, age) -> None:
		self.name = name
		self.age = age

	def get_stats(self):
		return f"Name{self.name}\nAge: {self.age}"


		
		