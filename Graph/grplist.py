#Adjacency list
from queue import LifoQueue
from queue import Queue


class Graph:
    def __init__(self,vertex=None):
        self.vertex=vertex
        self.data = [[] for _ in range(self.vertex)]
        
    def addedges(self, edge): #Add edges
        for n1, n2 in edge:
            self.data[n1].append(n2)
            self.data[n2].append(n1)
        return

    def deledges(self, edge):
        for n1, n2 in edge:
            self.data[n1].remove(n2)
            self.data[n2].remove(n1)
        return 

    def __repr__(self):
        return "\n".join(["{}: {}".format(node, neighbor) for node, neighbor in enumerate(self.data)])

    def __str__(self):
        return self.__repr__()

    def BFS(self, root):
        q = Queue()
        res =[]
        discovered =[False]*self.vertex
        distance =[None]*self.vertex
        discovered[root]=True
        distance[root]=0
        q.put(root)
        while q.empty() is False:
            current= q.get()
            res.append(current)
            for node in self.data[current]:
                if discovered[node]==False:
                    discovered[node]=True
                    distance[node]=1+ distance[current]
                    q.put(node)
        return res, distance

    def DFS(self, root):
        stack= []
        discovered =[False]*self.vertex
        result = []
        stack.append(root)
        while len(stack)>0:
            top = stack[len(stack)-1]
            stack.pop()
            result.append(top)
            discovered[top]=True
            for node in self.data[top]:
                if discovered[node]==False:
                    stack.append(node)
                    discovered[node]=True
        return result
                





                

        


g =Graph(5)
g.addedges([(0,1),(1,2),(0,2),(2,4),(3,4)])
#print("Original graph: ", g) 
print("BFS")
print(g.BFS(0))
print("DFS")
print(g.DFS(0))

        