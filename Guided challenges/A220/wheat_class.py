from crop_class import *
class Wheat(Crop):
	"""A wheat crop"""


	def __init__(self):
		super().__init__(2,5,4)
		self._type = "Wheat"

	def grow(self,light,water):
		if light >= self._light_need and water >= self._water_need:
			if self._status == "Seedling":
				self._growth += self._growth_rate * 1.5
			elif self._status == "Young":
				self._growth += self._growth_rate *1.25
			elif self._status == "Old":
				self._growth += self._growth_rate / 2
			else:
				self._growth += self._growth_rate
		self._days_growing += 1
		self._update_status()


def main():
	wheat_crop = Wheat()
	print(wheat_crop.report())
	manual_grow(wheat_crop)
	print(wheat_crop.report())
	auto_grow(wheat_crop,15)
	print(wheat_crop.report())

if __name__ == '__main__':
	main()
