from collections import defaultdict
class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.graph = defaultdict(list)

    def addEdge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    def printGraph(self):
        for i in range(self.vertices):
            print(self.graph[i])


    def bfs(self, x):
        queue = []
        visited = []
        queue.append(x)
        while queue:
            popped = queue.pop(0)
            visited.append(popped)
            for neighbor in self.graph[popped]:
                if neighbor not in visited:
                    queue.append(neighbor)
        print(visited)

    def shortestPath(self, source, destination):
        queue = []
        visited = []
        queue.append(source)
        while queue:
            popped = queue.pop(0)
            if popped == destination:
                return True
            visited.append(popped)
            for neighbor in self.graph[popped]:
                if neighbor not in visited:
                    queue.append(neighbor)
        return False

graph = Graph(4)
graph.addEdge(0,1)
# graph.addEdge(0,2)
graph.addEdge(0,3)
# graph.addEdge(2,1)
graph.addEdge(1,3)

graph.printGraph()
# graph.bfs(0)
print(graph.shortestPath(0,2))