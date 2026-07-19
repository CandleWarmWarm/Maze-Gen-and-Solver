from maze_gen.maze import Maze
# from solver import bfs
# from display import show

# def main():
# 	maze = load_maze()
# 	path = bfs(maze)
# 	show(maze, path)

# if __name__ == "__main__":
# 	main()

maze = Maze(5,5)

for row in maze.grid:
	for cell in row:
		print(cell.x, cell.y)