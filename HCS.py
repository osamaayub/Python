graph={'A':[(8,'B'),(20,'C')],
       'B':[(25,'A'),(20,'C'),(6,'D')],
       'C':[(25,'A'),(8,'B'),(12,'E')],
       'D':[(8,'B'),(12,'E'),(0,'F')],
       'E':[(20,'C'),(6,'D'),(0,'F')],
       'F':[(6,'D'),(12,'E')]
}
def HillClimbing(graph,startNode,goalNode):
    queue=[startNode]
    visited=[]
    success=[startNode]
    while queue:
         node=queue.pop(queue.index(min(queue)))
         if node[1] not in visited:
            size = len(success)-1
            if node[0] <= success[size-1][0]:
                visited.append(node[1])
                success.append(node)
            else:
                print("Goal not found.")
                return
         if node[1] == goalNode:
            return visited
         for n in (graph[node[1]]):
            queue.append(n)
    return visited


path=HillClimbing(graph,(25,'A'),'F')
print("path is:",path)
               
               
         
     
    