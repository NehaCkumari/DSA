#Graph Representation
# Adjacency list

class Graph:
    def __init__(self,vertex,edges):
        self.vertex=vertex
        self.data = [[] for _ in range(vertex)]
        for n1, n2 in edges:
            self.data[n1].append(n2)
            self.data[n2].append(n1)

    def __repr__(self):
        return "\n".join(["{}: {}".format(node, neighbor) for node, neighbor in enumerate(self.data)])

    def __str__(self):
        return self.__repr__()

V=5
edge = [(1,2),(2,3),(1,3),(2,4)]
g = Graph(V, edge)
print(g)





