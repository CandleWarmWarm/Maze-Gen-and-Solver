class AsciiDisplay:
	def show(self, maze):
		top = ""
		for x in range(maze.width):
			top += "o---"
		top += "o"
		print(top)

		for y in range(maze.height):
			middle = ""
			bottom = "o"
			for x in range(maze.width):
				cell = maze.grid[y][x]
				if x == 0 and y != 0:
					middle += "|"
				elif x == 0 and y == 0:
					middle += " "
				if cell.walls["right"]:
					middle += "   |"
				else:
					middle += "    "
			print(middle)
			for x in range(maze.width):
				cell = maze.grid[y][x]
				if cell.walls["bottom"]:
					bottom += "---o"
				else:
					bottom += "   o"
			print(bottom)
