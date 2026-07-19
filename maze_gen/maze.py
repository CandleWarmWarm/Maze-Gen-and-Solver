from maze_gen.cell import Cell

class Maze:
	def __init__(self, width, height):
		self.width = width
		self.height = height

		self.grid = []

		for y in range(height):
			row = []

			for x in range(width):
				row.append(Cell(x, y))

			self.grid.append(row)