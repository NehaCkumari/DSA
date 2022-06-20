class Graph:
    def __init__(self, vertex, wgt=False, direction=False):
        self.vertex=vertex
        self.wgt=wgt
        self.direction=direction
        self.data=[[] for _ in range(self.vertex)]
        
    def addedges(self, edge):
        if self.wgt:
            for n1, n2, wt in edge:
                if self.direction:
                    self.data[n1].append((n2,wt))
                else:
                    self.data[n1].append((n2,wt))
                    self.data[n2].append((n1,wt))
        else:
            for n1, n2 in edge:
                if self.direction:
                    self.data[n1].append((n2))
                else:
                    self.data[n1].append(n2)
                    self.data[n2].append(n1)
        return 

    def __repr__(self):
        return "\n".join(["{}: {}".format(node, neighbor) for node, neighbor in enumerate(self.data)])

    def __str__(self):
        return self.__repr__()
        
V=5
edges_wt=[(1,2,4),(0,3,6)]
edges =[(0,1),(2,1)]
W=True
D=True

g =Graph(V)
g.addedges(edges)
print(g)



        