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

def Create_maze(Size, branch_chance, rows, columns):
    maze = []
    grid = []
    #create genesis first child.
    Genesis_Node = Node("unexplored", None, None)
    maze.append(Genesis_Node)

    No_Child = [Genesis_Node]

    for x in range(rows):
        for y in range(columns):
            new_cell = cell(x, y, None)
            grid.append(new_cell)

    Genesis_Node.state = (random.randrange(rows), random.randrange(columns))







    for i in range(Size - 1):
        #print(f"size_of_mize: {len(maze)}no_child = {len(No_Child)}, maze: {No_Child}")
        new_parent = random.choice(No_Child)


        new_node = Node("unexplored", new_parent , "retiring")
        if random.random() > branch_chance:
            No_Child.remove(new_parent)

        No_Child.append(new_node)
        maze.append(new_node)
    return maze

new_maze = Create_maze(12, 0.8, 5, 5)







frontier = StackFrontier()

