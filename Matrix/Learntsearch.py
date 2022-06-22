#Write an efficient algorithm that searches for a value target in an m x n integer matrix matrix. 
# This matrix has the following properties:
#Integers in each row are sorted from left to right.
#The first integer of each row is greater than the last integer of the previous row.

def search(mat, target):
    R=len(mat)
    B=len(mat[0])
    T=0
    L=0
    if R==1 and B==1:
        if mat[0]==target:
            return True
        else:
            return False
    while L!=R-1 and T!=B-1:
        midc=int((L+R)/2)
        if mat[T][midc]==target:
            return True
        elif mat[T][midc]<target:
            L=midc
        else:
            R=midc
        midr=int((T+B)/2)
        if mat[midr][L]==target:
            return True
        elif mat[midr][L]<target:
            T=midr
        else:
            B=midr
    return False


mat=[[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target=10
print(search(mat,target))