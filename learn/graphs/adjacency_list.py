# This represents the nodes which are connected to a given vertex
class Node:
    def __init__(self, data):
        self.vertex = data
        self.next = None

class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.graphArray = [None] * self.vertices;

    def add_edge(self, src, dest):
        node = Node(dest)
        node.next = self.graphArray[src]
        self.graphArray[src] = node

        node = Node(src)
        node.next = self.graphArray[dest]
        self.graphArray[dest] = node

    def print_graph(self):
        for i in range(self.vertices):
            print('Adjacency list for vertex {} '.format(i))
            if self.graphArray[i] is not None:
                temp = self.graphArray[i] 
                while temp:
                    print('-> {}' . format(temp.vertex))
                    temp = temp.next
    
    def bfs(self, vertex):
        visited = [False] * self.vertices
        queue = []

        queue.append(vertex)
        visited[vertex] = True

        while queue:
            popped = queue.pop(0)
            print(popped)
            if self.graphArray[popped]:
                temp = self.graphArray[popped]
                result = temp.vertex
                while temp:
                    if visited[result]:
                       temp = temp.next
                    else:
                        visited[result] = True
                        queue.append(result)
                        temp = temp.vertex
        

graph = Graph(5)
graph.add_edge(0, 1)
graph.add_edge(0, 4)
graph.add_edge(1, 2)
graph.add_edge(1, 3)
graph.add_edge(1, 4)
graph.add_edge(2, 3)
graph.add_edge(3, 4)
 
# graph.print_graph()

graph.bfs(2)

