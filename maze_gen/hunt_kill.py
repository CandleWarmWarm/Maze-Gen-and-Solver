from maze_gen.maze import Maze
import random

class HuntAndKill:
	def __init__(self,maze):
		self.maze = maze
	
	def hunt(self):

		for y in range(self.maze.height):
			for x in range(self.maze.width):
				cell = self.maze.grid[y][x]
				if cell.visited  == False :
					neighbors = self.maze.get_neighbors(cell)
					for neighbor in neighbors:
						if neighbor.visited:
							self.maze.remove_wall(cell, neighbor)
							cell.visited = True
							return cell
		return None
					
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
				current = self.hunt()
				
				if current is None:
					break