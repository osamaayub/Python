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
def dfs(graph,startNode):
    stack,visited=[startNode],[]
    while stack:
        vertex=stack.pop(0)
        for edge in graph[vertex]:
            if edge not in visited:
                visited.append(edge)
                stack.append(edge)
        return visited

print(dfs(graph,'S'))