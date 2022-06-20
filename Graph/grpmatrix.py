#Adjacency matrix
class Graph:
    def __init__(self,vertex=None):
        self.row=vertex
        self.col=vertex
        self.data = [[0 for i in range(self.row)] for j in range(self.col)]
        
    def addedges(self, edge): #Add edges
        for n1, n2 in edge:
            self.data[n1][n2]=1
            self.data[n2][n1]=1
        return

    def deledges(self, edge):
        for n1, n2 in edge:
            self.data[n1][n2]=0
            self.data[n2][n1]=0
        return 

    def __repr__(self):
        return "\n".join(["{}: {}".format(node, neighbor) for node, neighbor in enumerate(self.data)])

    def __str__(self):
        return self.__repr__()

g=Graph(4)
g.addedges([(0,1),(1,3)])
print(g)
g.deledges([(0,1)])
print(g)
        