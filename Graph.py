

class Graph:
    graph = {}
    vertices = 0

    def __init__(self):
        self.__vertices = 0
        self.__graph = {}

    def addVertex(self, ver):
        self.__vertices = self.__vertices+1
        self.__graph[ver] = []

    def addEdge(self, ver1, ver2, edgde):
        temp = [ver2, edgde]
        self.__graph[ver1].append(temp)

    def display(self):
        for vertex in self.__graph:
            for edge in self.__graph[vertex]:
                print(vertex, "->", edge[0], "->", edge[1])


Graph2 = Graph()
Graph2.addVertex(1)
Graph2.addVertex(2)
Graph2.addVertex(3)
Graph2.addVertex(4)
Graph2.addVertex(5)
Graph2.addEdge(1, 2, 5)
Graph2.addEdge(2, 1, 10)
Graph2.addEdge(2, 5, 8)
Graph2.addEdge(3, 2, 7)
Graph2.display()
