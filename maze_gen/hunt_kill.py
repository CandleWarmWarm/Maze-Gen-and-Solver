from maze_gen.maze import Maze
import random

class HuntAndKill:
	def __init__(self,maze):
		self.maze = maze

	def generate(self):
		current = self.maze.grid[0][0]
		current.visited = True

		while True:
			neighbors = self.maze.get_neighbors(current)
			unvisited = []
			for neighbor in neighbors:
				if neighbor.visited == False :
					unvisited.append(neighbor)
			if unvisited:
				next = random.choice(unvisited)
				self.maze.remove_wall(current, next)
				next.visited = True
				current = next
			else :
				break

