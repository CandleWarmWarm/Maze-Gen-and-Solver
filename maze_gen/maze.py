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
	
	def get_neighbors(self, cell):
		neighbors = []

		x = cell.x
		y = cell.y

		# Top
		if y > 0:
			neighbors.append(self.grid[y - 1][x])

		# Bottom
		if y < self.height - 1:
			neighbors.append(self.grid[y + 1][x])

		# Left
		if x > 0:
			neighbors.append(self.grid[y][x - 1])

		# Right
		if x < self.width - 1:
			neighbors.append(self.grid[y][x + 1])

		return neighbors
	
	def remove_wall(self, current, next):
		#next = top side
		if next.y == current.y - 1:
			current.walls["top"] = False
			next.walls["bottom"] = False

		#next = bottom side
		if next.y == current.y + 1:
			current.walls["bottom"] = False
			next.walls["top"] = False

		#next = left side
		if next.x == current.x - 1:
			current.walls["left"] = False
			next.walls["right"] = False

		#next = right side
		if next.x == current.x + 1:
			current.walls["right"] = False
			next.walls["left"] = False
