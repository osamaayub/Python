graph={
    'S' : ['A','C','D'],
    'A' : [],
    'B' : ['E'],
    'C' : ['F'],
    'D' : ['B','G'],
    'E' : ['G'],
    'F' : ['E','G'],
    'G' : []
}
def bfs(graph,startNode):
    queue,visited=[startNode],[]
    while queue:
        vertex=queue.pop(0)
        for edge in graph[vertex]:
            if edge not in visited:
                visited.append(edge)
                queue.append(edge)
        return visited

print(bfs(graph,'S'))