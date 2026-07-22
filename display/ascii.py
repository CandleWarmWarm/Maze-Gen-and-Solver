class AsciiDisplay:
	def show(self, maze):
		for y in range(maze.height):
			line = ""
			for x in range(maze.width):
				line += "o---"
			line += "o"
			print(line)
			row = ""
			for x in range(maze.width):
				row += "|   "
			row += "|"
			print(row)
		line = ""
		for x in range(maze.width):
			line += "o---"
		line += "o"
		print(line)