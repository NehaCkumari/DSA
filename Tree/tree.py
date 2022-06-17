#Binary tree
import queue


class BinaryTree:
    def __init__(self,data,left=None,right=None):
        self.data=data
        self.left=left
        self.right=right



    
Root=BinaryTree(10)
lchild=BinaryTree(9)
rchild=BinaryTree(1)
llchild=BinaryTree(5)
lrchild=BinaryTree(12)
rlchild=BinaryTree(16)
rrchild=BinaryTree(2)
Root.left=lchild
Root.right=rchild
lchild.left=llchild
lchild.right=lrchild
rchild.left=rlchild
rchild.right=rrchild

def preOrdertraverse(Treenode):
    if Treenode==None:
        return
    else:
        print(Treenode.data)
        preOrdertraverse(Treenode.left)
        preOrdertraverse(Treenode.right)
    return
print("\nPreOrder")
preOrdertraverse(Root)

def postOrdertraverse(Treenode):
    if Treenode==None:
        return
    else:
        postOrdertraverse(Treenode.left)
        postOrdertraverse(Treenode.right)
        print(Treenode.data)
    return
print("\nPostOrder")
postOrdertraverse(Root)
def InOrdertraverse(Treenode):
    if Treenode==None:
        return
    else:
        postOrdertraverse(Treenode.left)
        print(Treenode.data)
        postOrdertraverse(Treenode.right)
        
    return
print("\nInOrder")
InOrdertraverse(Root)

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
print("\nleveltraverse")
print(leveltraverse(Root))
    


