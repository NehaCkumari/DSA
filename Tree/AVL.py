class Node:
    def __init__(self,data=None,key=0):
        self.data=data
        self.left=None
        self.right=None
        self.key=key

class AVL:
    def __init__(self):
        pass

    def addchild(self, root, value):
        if self==None:
            self.data=value
            return
        else:
            if value<root.data:
                if root.left==None:
                    root.left=Node(value)
                    return
                else:
                    self.addchild(root.left,value)

            else:
                if root.right==None:
                    root.right=Node(value)
                    return
                else:
                    self.addchild(root.right,value)

        def preOrder(self,root):
            if root==None:
                return
            else:
                self.preOrder(root.left)
                print(root.data)
                self.preOrder(root.right)
            

        def getheight(self,root):
            if root==None:
                return -1
            else:
                lheight=self.getheight(root.left)
                rheight=self.getheight(root.right)
                height=1+max(lheight,rheight)

tree=AVL()
root=Node()
root=tree.addchild(root,5)
root=tree.addchild(root,4)
root=tree.addchild(root,10)
root=tree.addchild(root,1)
tree.preOrder(root)



            
    
                




    

    

