#Implement Greedy  Best Search
from queue import heappop,heappush
from math import inf
class Graph:
    def __init__(self, directed=True):
        self.edges = {}
        self.huristics = {}
        self.directed = directed

    def add_edge(self, node1, node2, cost=1, __reversed=False):
        try:
            neighbors = self.edges[node1]
        except KeyError:
            neighbors = {}
        neighbors[node2] = cost
        self.edges[node1] = neighbors
        if not self.directed and not __reversed:
            self.add_edge(node2, node1, cost, True)

    def set_huristics(self, huristics={}):
        self.huristics = huristics

    def neighbors(self, node):
        try:
            return self.edges[node]
        except KeyError:
            return []

    def cost(self, node1, node2):
        try:
            return self.edges[node1][node2]
        except:
            return inf

    def best_first_search(self, start, goal):
        found, fringe, visited, came_from, cost_so_far = False, [
            (self.huristics[start], start)], set([start]), {start: None}, {start: 0}
        print('{:11s} | {}'.format('Expand Node', 'Fringe'))
        print('--------------------')
        print('{:11s} | {}'.format('-', str(fringe[0])))
        while not found and len(fringe):
            _, current = heappop(fringe)
            print('{:11s}'.format(current), end=' | ')
            if current == goal:
                found = True
                break
            for node in self.neighbors(current):
                new_cost = cost_so_far[current] + self.cost(current, node)
                if node not in visited or cost_so_far[node] > new_cost:
                    visited.add(node)
                    came_from[node] = current
                    cost_so_far[node] = new_cost
                    heappush(fringe, (new_cost + self.huristics[node], node))
            print(', '.join([str(n) for n in fringe]))
        if found:
            print()
            return came_from, cost_so_far[goal]
        else:
            print('No path from {} to {}'.format(start, goal))
            return None, inf

    @staticmethod
    def print_path(came_from, goal):
        parent = came_from[goal]
        if parent:
            Graph.print_path(came_from, parent)
        else:
            print(goal, end='')
            return
        print(' =>', goal, end='')

    def __str__(self):
        return str(self.edges)


graph = Graph(directed=True)
graph.add_edge('S', 'A', 3)
graph.add_edge('S', 'B', 2)
graph.add_edge('A', 'C', 4)
graph.add_edge('A', 'D', 1)
graph.add_edge('B', 'E', 3)
graph.add_edge('B', 'F', 1)
graph.add_edge('E', 'H', 5)
graph.add_edge('F', 'I', 2)
graph.add_edge('F', 'G', 3)
graph.set_huristics({'A': 12, 'B': 4, 'C': 7, 'D': 3,
                    'E': 8, 'F': 2, 'H': 4, 'I': 9, 'S': 13, 'G': 0})
start, goal = 'S', 'G'
traced_path, cost = graph.best_first_search(start, goal)
if (traced_path):
    print('Path:', end=' ')
    Graph.print_path(traced_path, goal)
    print('\nCost:', cost)
