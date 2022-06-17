class BST:
    def __init__(self,data=None):
        self.data=data
        self.left=None
        self.right=None

    def addchild(self,temp,value):
        if self.data==None:
            self.data=value
            return
        else:
            node=BST(value)
            if value<temp.data:
                if temp.left==None:
                    temp.left=node
                    return
                else:
                    self.addchild(temp.left,value)
            else:
                if temp.right==None:
                    temp.right=node
                    return
                else:
                    self.addchild(temp.right,value)
        return
def postOrdertraverse(Treenode):
    if Treenode==None:
        return
    else:
        postOrdertraverse(Treenode.left)
        postOrdertraverse(Treenode.right)
        print(Treenode.data)
    return

def leveltraverse(Treenode,level=0):
    if Treenode==None:
        return
    else:
        queue=[]
        queue.append(Treenode)
        while(len(queue)>0):
            print(queue[0].data)
            node=queue.pop(0)
            if node.left is not None:
                leveltraverse(node.left)
            if node.right is not None:
                leveltraverse(node.right)
    return


root=BST(5)
root.addchild(root,2)
root.addchild(root,6)
root.addchild(root,1)
root.addchild(root,8)
postOrdertraverse(root)
print("leveltransverse")
leveltraverse(root)  
        
