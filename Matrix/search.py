#Write an efficient algorithm that searches for a value target in an m x n integer matrix matrix. 
# This matrix has the following properties:
#Integers in each row are sorted from left to right.
#The first integer of each row is greater than the last integer of the previous row.

def targetsearch(mat, target):
    row=len(mat)
    col=len(mat[0])
    l=0
    r=col-1
    t=0
    b=row-1
    res=False
    while(l<r and t<b):
        while(l<r):
            vmid=int((l+r)/2)
            if target==mat[l][vmid]:
                res=True
            elif target<mat[l][vmid]:
                r=vmid
            else:
                l=vmid
        while(t<b):
            hmid=int((t+b)/2)
            if target==mat[hmid][t]:
                res=True
            elif target<mat[hmid][t]:
                b=hmid
            else:
                t=hmid
    return res

mat=[[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target=10
print(targetsearch(mat,target))