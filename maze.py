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
            self.take_last_added()

def Create_maze(Size, branch_chance):
    maze = []
    #create genesis first child.
    Genesis_Node = Node("unexplored", None, None)
    maze.append(Genesis_Node)

    No_Child = [Genesis_Node]
    for i in range(Size - 1):
        print(f"size_of_mize: {len(maze)}no_child = {len(No_Child)}, maze: {No_Child}")
        new_parent = random.choice(No_Child)


        new_node = Node("unexplored", new_parent , "retiring")
        if random.random() > branch_chance:
            No_Child.remove(new_parent)

        No_Child.append(new_node)
        maze.append(new_node)
    return maze

new_maze = Create_maze(12, 0.8)







frontier = StackFrontier()

maze = Create_maze(12, 0.15)