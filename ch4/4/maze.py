import copy

MAZE = [
    [9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9],
    [9, 0, 0, 0, 9, 0, 0, 0, 0, 0, 0, 9],
    [9, 0, 9, 0, 0, 0, 9, 9, 0, 9, 9, 9],
    [9, 0, 9, 9, 0, 9, 0, 0, 0, 9, 0, 9],
    [9, 0, 0, 0, 9, 0, 0, 9, 9, 0, 9, 9],
    [9, 9, 9, 0, 0, 9, 0, 9, 0, 0, 0, 9],
    [9, 0, 0, 0, 9, 0, 9, 0, 0, 9, 1, 9],
    [9, 0, 9, 0, 0, 0, 0, 9, 0, 0, 9, 9],
    [9, 0, 0, 9, 0, 9, 0, 0, 9, 0, 0, 9],
    [9, 0, 9, 0, 9, 0, 9, 0, 0, 9, 0, 9],
    [9, 0, 0, 0, 0, 0, 0, 9, 0, 0, 0, 9],
    [9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9]
]

class Maze1:
    def __init__(self, maze):
        self.maze = maze

    def search(self, x, y):
        pos = [[x, y, 0]]
        while len(pos) > 0:
            x, y, depth = pos.pop(0)

            if self.maze[x][y] == 1:
                return depth

            self.maze[x][y] = 2

            if self.maze[x - 1][y] < 2:
                pos.append([x - 1, y, depth + 1])
            if self.maze[x + 1][y] < 2:
                pos.append([x + 1, y, depth + 1])
            if self.maze[x][y - 1] < 2:
                pos.append([x, y - 1, depth + 1])
            if self.maze[x][y + 1] < 2:
                pos.append([x, y + 1, depth + 1])

class Maze2:
    def __init__(self, maze):
        self.maze = maze

    def search(self, x, y, depth=0):
        if self.maze[x][y] == 1:
            return depth

        self.maze[x][y] = 2

        if self.maze[x - 1][y] < 2:
            res = self.search(x - 1, y, depth + 1)
            if res:
                return res
        if self.maze[x + 1][y] < 2:
            res = self.search(x + 1, y, depth + 1)
            if res:
                return res
        if self.maze[x][y - 1] < 2:
            res = self.search(x, y - 1, depth + 1)
            if res:
                return res
        if self.maze[x][y + 1] < 2:
            res = self.search(x, y + 1, depth + 1)
            if res:
                return res

        self.maze[x][y] = 0

class Maze3:
    def __init__(self, maze):
        self.maze = maze

    def search(self, x, y):
        dir = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        x, y, depth, d = 1, 1, 0, 0

        while self.maze[x][y] != 1:
            self.maze[x][y] = 2

            for i in range(len(dir)):
                j = (d + i - 1) % len(dir)
                if self.maze[x + dir[j][0]][y + dir[j][1]] < 2:
                    x += dir[j][0]
                    y += dir[j][1]
                    d = j
                    depth += 1
                    break
                elif self.maze[x + dir[j][0]][y + dir[j][1]] == 2:
                    x += dir[j][0]
                    y += dir[j][1]
                    d = j
                    depth -= 1
                    break

        return depth

maze1 = Maze1(copy.deepcopy(MAZE))
print(maze1.search(1, 1))

maze2 = Maze2(copy.deepcopy(MAZE))
print(maze2.search(1, 1))

maze3 = Maze3(copy.deepcopy(MAZE))
print(maze3.search(1, 1))
