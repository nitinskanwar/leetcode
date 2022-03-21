class Graph:
    def __init__(self, size):
        self.vertices = size
        self.graph = defaultdict(list)
        self.paths = []
        
    def addEdge(self, u, v):
        self.graph[u].append(v)
    
    def findPath(self, source, destination, visited, path):
        visited.append(source)
        path.append(source)
        
        if source == destination:
            print(path)
            self.paths.append(path)
        else:
            for i in self.graph[source]:
                if i not in visited:
                    self.findPath(i, destination, visited, path)
                            
        visited.pop()
        path.pop()
        
class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        gf = Graph(len(graph))
        for i in range(len(graph)):
            for j in graph[i]:
                gf.addEdge(i,j)
        
        for i in range(len(graph)):
            print(i, gf.graph[i])
        gf.findPath(0, len(graph)-1,[],[])
        print(gf.paths)