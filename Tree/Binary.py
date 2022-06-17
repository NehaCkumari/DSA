#Binary tree
import queue


class BinaryTree:
    def __init__(self,data,left=None,right=None):
        self.data=data
        self.left=left
        self.right=right

    def preOrdertraverse(self,root):
        if root==None:
            return
        else:
            print(root.data)
            self.preOrdertraverse(root.left)
            self.preOrdertraverse(root.right)
        return


    
Drink=BinaryTree("Drink")
Hot=BinaryTree("Hot")
Cold=BinaryTree("Cold")
#Cola=BinaryTree("Cola")
#Tea=BinaryTree("Tea")
#MasalaTea=BinaryTree("MasalaTea")
Drink.left=Hot
Drink.right=Cold
#Hot.left=Tea
#Hot.right=MasalaTea
#Cold.left=Cola

print("\nPreOrder")
Drink.preOrdertraverse(Drink)

def postOrdertraverse(Treenode):
    if Treenode==None:
        return
    else:
        postOrdertraverse(Treenode.left)
        postOrdertraverse(Treenode.right)
        print(Treenode.data)
    return
print("\nPostOrder")
postOrdertraverse(Drink)
def InOrdertraverse(Treenode):
    if Treenode==None:
        return
    else:
        postOrdertraverse(Treenode.left)
        print(Treenode.data)
        postOrdertraverse(Treenode.right)
        
    return
print("\nInOrder")
InOrdertraverse(Drink)

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
print(leveltraverse(Drink))
    


