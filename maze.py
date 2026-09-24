import random
class Node():
    def __init__(self, state, parent, action):
        self.state = state
        self.parent = parent
        self.action = action


class StackFrontier():
    def __init__(self):
        self.frontier = []
    def add(self, node):
        self.frontier.append(node)
    def reset(self):
        self.frontier = []

    def take_last_added(self):
        latest_added = self.frontier[-1]
        self.frontier.remove(self.frontier[-1])
        return  latest_added
    def empty(self):
        return len(self.frontier) == 0
    def remove(self):
        if self.empty():
            raise  Exception("Empty Frontier")
        else:
            return self.take_last_added()


class cell():
    def __init__(self, row, col, val):
        self.row = row
        self.col = col
        #The values should represent possible states, e.g 0 = wall(no node), 1 = genesis node so start there, 2 = regular node, 3 = goal(could be multiple)

        self.val = val

def check_options(cell, grid):

    options = []
    x = cell.row
    y = cell.col

    def cycle_through(types):
        for c, v in types:
            row_is_valid = 0 <= c < len(grid)

            if row_is_valid:
                column_is_valid = 0 <= v < len(grid[c])

                if column_is_valid and grid[c][v].val == 0:
                    options.append((c, v))

    cycle_through([(x + 1, y), (x - 1, y), ( x, y - 1), (x, y+ 1) ])




    print(f"options: {options}")
    return  options


def Create_maze(Size, branch_chance, rows, columns):
    maze = []
    grid = []
    #create genesis first child.
    Genesis_Node = Node("unexplored", None, None)
    maze.append(Genesis_Node)


    for x in range(rows):

        grid.append(x)
        grid[x] = []
        for y in range(columns):
            new_cell = cell(x, y, 0)
            grid[x].append(y)
            grid[x][y] = new_cell

    Genesis_Node.state = (random.randrange(rows), random.randrange(columns))

    u, i = Genesis_Node.state
    grid[u][i].val = 1
    options = check_options(grid[u][i], grid)
    branches = []
    branches.append(grid[u][i])



    for i in range(Size - 1):

        for branch in branches:
            options = check_options(grid[branch.row][branch.col], grid)
            if options:
                if len(options) == 0:
                    print("Removing branch")
                    branches.remove(branch)

        #print(f"size_of_mize: {len(maze)}no_child = {len(No_Child)}, maze: {No_Child}")
        new_node = Node("unexplored", random.choice(branches), "retiring")

        #We check for the options of the new nodes parents so we know where it can be placed.


        options = check_options(grid[new_node.parent.row][new_node.parent.col], grid)
        print(f"options created second = {options}")


        if options:
            l, k = random.choice(options)

            grid[l][k].val = 2
            print("NEW CELL MADE")
            if random.random() < branch_chance:
                print("branching")
                options = check_options(grid[l][k], grid)
                if len(options) >= 2:
                    branches.append(grid[l][k])

            branches.remove(new_node.parent)
            branches.append(grid[l][k])
            maze.append(new_node)

    goal = random.choice(branches)
    grid[goal.row][goal.col].val = 3
    return maze, grid

rows = 5
columns = 5
new_maze, new_grid = Create_maze(12, 0.8, rows, columns)
for x in range(rows):
    list = []
    for y in range(columns):
        list.append(new_grid[x][y].val)

    print(list)


frontier = StackFrontier()
