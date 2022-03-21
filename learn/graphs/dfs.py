from collections import defaultdict
class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.graph = defaultdict(list)

    def addEdge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)
    
    def dfs_stack(self, u):
        stack = []
        visited = []

        stack.append(u)
        while stack:
            current = stack.pop()
            if current not in visited:
                print(current)
                visited.append(current)
            for i in self.graph[current]:
                if i not in visited:
                    stack.append(i)
        return visited

    def dfs_recursion(self, u, visited):
        if u not in visited:
            visited.append(u)
        for i in self.graph[u]:
            if i not in visited:
                visited = self.dfs_recursion(i, visited)
        return visited

    def traverseAllPaths(self, start, finish, visited, path):
        visited.append(start)
        path.append(start)

        if start == finish:
            print('Path is :')
            print(path)
        else:
            for i in self.graph[start]:
                if i not in visited:
                    self.traverseAllPaths(i, finish, visited, path)
        
        path.pop()
        visited.pop()
        

graph = Graph(4)
graph.addEdge(0,1)
graph.addEdge(0,2)
graph.addEdge(0,3)
graph.addEdge(2,0)
graph.addEdge(2,1)
graph.addEdge(1,3)

# print(graph.dfs_stack(1))
# print(graph.dfs_recursion(1,[]))
visited = [False] * (4)
graph.traverseAllPaths(0,3,[],[])
