class Cell:
	def __init__(self,x,y):

		self.x = x
		self.y = y

		self.visited = False

		self.walls = {
			"top": True,
			"bottom": True,
			"left": True,
			"right": True
		}