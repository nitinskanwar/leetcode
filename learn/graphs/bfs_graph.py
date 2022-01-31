import adjacency_list as ajd_list

class Traversal:
    def __init__(self):
        

graph = ajd_list.Graph(5)
graph.add_edge(0, 1)
graph.add_edge(0, 4)
graph.add_edge(1, 2)
graph.add_edge(1, 3)
graph.add_edge(1, 4)
graph.add_edge(2, 3)
graph.add_edge(3, 4)
 
graph.print_graph()