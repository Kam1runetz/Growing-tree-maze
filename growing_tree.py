from random import randint, choice

# from pprint import pprint

# !!! КОПИПАСТА ПРЕСЛЕДУЕТСЯ АНАЛЬНЫМИ КАРАМИ

OPEN = True
CLOSE = False


class Cell(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        # self._matrix = matrix
        self.left = CLOSE
        self.right = CLOSE
        self.up = CLOSE
        self.down = CLOSE
        self.is_visited = False
        # self._directions = {'left': OPEN, 'right': OPEN, 'top': OPEN, 'bottom': OPEN}

    # def __repr__(self):
    # return 'C({}, {})'.format(self.x, self.y)

    # property


# def left(self):
#    return self._directions['left']

# property
# def right(self):
#   return self._directions['right']

# property
# def up(self):
#   return self._directions['top']

# property
# def down(self):
#   return self._directions['bottom']

# def neighbours(self):
#   n = []
#  if (self.x > 0) and (self._matrix[self.y][self.x - 1].is_visited is False):
#     n.append('left')
# if (self.x < width - 1) and (self._matrix[self.y][self.x + 1].is_visited is False):
#   n.append('right')
# if (current_cell.y > 0) and (maze[current_cell.y - 1][current_cell.x].is_visited is False):
#   n.append('bottom')
# if (current_cell.y < height - 1) and (maze[current_cell.y + 1][current_cell.x].is_visited is False):
#   n.append('top')
# return n

# direction = property()

# direction.getter
#   def direction(self, neighbour, value):
#        self._directions[neighbour] = value

# direction.setter
# def direction(self, neighbour):
#   return self._directions[neighbour]

class Stack(object):
    def __init__(self):
        self.arr = []

    def push(self, value):
        self.arr.append(value)

    def pop(self):
        res = self.arr[-1]
        del self.arr[-1]
        return res

    def is_empty(self):
        if len(self.arr) == 0:
            return True
        else:
            return False


def create_raw_maze(height, width):
    raw_maze = [0] * height
    for i in range(height):
        raw_maze[i] = [0] * width

    for i in range(height):
        for j in range(width):
            raw_maze[i][j] = Cell(j, i)
    return raw_maze


def visual_maze(maze, height, width):
    str_maze = ''
    for _ in range(width):
        str_maze += '__'
    print(str_maze)
    for i in range(height):
        str_maze = ''
        for j in range(width):
            if (maze[i][j].right == CLOSE) and (maze[i][j].down == CLOSE):
                if j == 0:
                    str_maze += '|_|'
                else:
                    str_maze += '_|'
            elif (maze[i][j].right == CLOSE) and (maze[i][j].down == OPEN):
                if j == 0:
                    str_maze += '| |'
                else:
                    str_maze += ' |'
            elif (maze[i][j].right == OPEN) and (maze[i][j].down == CLOSE):
                if j == 0:
                    str_maze += '|__'
                else:
                    str_maze += '__'
            else:
                if j == 0:
                    str_maze += '|  '
                else:
                    str_maze += '  '
        print(str_maze)


def main():
    print("Enter height and width of maze: ")
    height, width = map(int, input().split())
    maze = create_raw_maze(height, width)
    path = Stack()
    current_cell = maze[0][0]
    current_cell.is_visited = True
    path.push(current_cell)

    while not path.is_empty():
        next_step = []
        if (current_cell.x > 0) and (maze[current_cell.y][current_cell.x - 1].is_visited is False):
            next_step.append(maze[current_cell.y][current_cell.x - 1])
        if (current_cell.x < width - 1) and (maze[current_cell.y][current_cell.x + 1].is_visited is False):
            next_step.append(maze[current_cell.y][current_cell.x + 1])
        if (current_cell.y > 0) and (maze[current_cell.y - 1][current_cell.x].is_visited is False):
            next_step.append(maze[current_cell.y - 1][current_cell.x])
        if (current_cell.y < height - 1) and (maze[current_cell.y + 1][current_cell.x].is_visited is False):
            next_step.append(maze[current_cell.y + 1][current_cell.x])

        if len(next_step) != 0:
            next_cell = next_step[randint(0, len(next_step) - 1)]

            if next_cell.x != current_cell.x:
                if current_cell.x - next_cell.x > 0:
                    maze[current_cell.y][current_cell.x].left = OPEN
                    maze[next_cell.y][next_cell.x].right = OPEN
                else:
                    maze[current_cell.y][current_cell.x].right = OPEN
                    maze[next_cell.y][next_cell.x].left = OPEN
            if next_cell.y != current_cell.y:
                if current_cell.y - next_cell.y > 0:
                    maze[current_cell.y][current_cell.x].up = OPEN
                    maze[next_cell.y][next_cell.x].down = OPEN
                else:
                    maze[current_cell.y][current_cell.x].down = OPEN
                    maze[next_cell.y][next_cell.x].up = OPEN

            next_cell.is_visited = True
            path.push(next_cell)
            current_cell = next_cell

        else:
            current_cell = path.pop()
    visual_maze(maze, height, width)


if __name__ == '__main__':
    main()

# def create_matrix(m, n):
#   return [[Cell(j, i) for j in range(n)] for i in range(m)]


# def generate_maze(columns, lines):
#  m = create_matrix(lines, columns)
# stack = [m[0][0]]
# while stack:
#   current_cell = stack.pop()

#  neighbours = current_cell.neighbours()

# if not neighbours:
#    continue

# n = choice(neighbours)
# current_cell.direction(n, OPEN)
# stack.append(current_cell)
# stack.append(n)


# def main():
# n = 10
# m = 10
# c = Cell(0, 0)
# print(c.get_available_directions())
#   m = generate_maze(n, m)


# if __name__ == '__main__':
#    main()
