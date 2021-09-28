from queue import heappop, heappush
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

    def a_star_search(self, start, goal):
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
graph.add_edge('A', 'B', 6)
graph.add_edge('A', 'F', 3)
graph.add_edge('B', 'D', 2)
graph.add_edge('B', 'C', 5)
graph.add_edge('C', 'E', 5)
graph.add_edge('C', 'D', 1)
graph.add_edge('D', 'E', 8)
graph.add_edge('D', 'C', 1)
graph.add_edge('E', 'I', 5)
graph.add_edge('E', 'J', 5)
graph.add_edge('I', 'G', 3)
graph.add_edge('I', 'J', 3)
graph.add_edge('I', 'H', 2)
graph.add_edge('H', 'I', 2)
graph.add_edge('H', 'F', 7)
graph.add_edge('F', 'G', 5)
graph.add_edge('F', 'A', 3)

graph.set_huristics({'A': 10, 'B': 8, 'C': 5, 'D': 7,
                    'E': 3, 'F': 6, 'G': 5, 'H': 3, 'I': 1, 'J': 0})
start, goal = 'A', 'J'
traced_path, cost = graph.a_star_search(start, goal)
if (traced_path):
    print('Path:', end=' ')
    Graph.print_path(traced_path, goal)
    print('\nCost:', cost)
