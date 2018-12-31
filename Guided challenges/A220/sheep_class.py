from animal_class import *

class Sheep(Animal):
	"""A simulation of a Sheep"""

	def __init__(self,name):
		super().__init__(3,3,2,name)

		self._type = "Sheep"
	def grow(self,food,water):
		if food > self._food_need:
			self._weight += self._growth_rate * 1.2
		elif food == self._food_need and water >= self._water_need:
			self._weight += self._growth_rate
		self._days_growing += 1
		self._update_status()

def main():
	new_Sheep = Sheep("Shaun")
	manage_animal(new_Sheep)

if __name__ == '__main__':
	main()
