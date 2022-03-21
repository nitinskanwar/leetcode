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
    
graph = Graph(6)
graph.add_edge(0, 1)
graph.add_edge(0, 2)
graph.add_edge(0, 5)
graph.add_edge(2, 1)
graph.add_edge(2, 3)
graph.add_edge(2, 4)
graph.add_edge(3, 4)
graph.add_edge(3, 5)

graph.print_graph()

