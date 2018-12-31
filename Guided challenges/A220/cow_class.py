from animal_class import *

class Cow(Animal):
	"""A simulation of a Cow"""


	def __init__(self,name):

		super().__init__(2,5,4,name)
		self._type = "Cow"


	def grow(self,food,water):
		if food > self._food_need:
			self._weight += self._growth_rate * 1.1
		elif food == self._food_need and water >= self._water_need:
			self._weight += self._growth_rate

		self._days_growing += 1

		self._update_status()

def main():

	new_cow = Cow("Jim")

	manage_animal(new_cow)

if __name__ == '__main__':
	main()
