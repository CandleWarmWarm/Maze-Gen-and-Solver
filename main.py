from maze_gen.maze import Maze
from maze_gen.hunt_kill import HuntAndKill
from display.ascii import AsciiDisplay


def main():
    maze = Maze(10, 5)

    generator = HuntAndKill(maze)
    generator.generate()

    display = AsciiDisplay()
    display.show(maze)


if __name__ == "__main__":
    main()