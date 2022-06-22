def spiral(mat):
    R=len(mat[0])
    B=len(mat)
    L=0
    T=0
    while(L!=R and T!=B):
        i=L
        while i<R:
            print(mat[T][i])
            i+=1
        T+=1
        j=T
        while j<B:
            print(mat[j][R-1])
            j+=1
        R-=1
        k=R-1
        while k>=L:
            print(mat[B-1][k])
            k-=1
        B-=1
        z=B-1
        while z>=T:
            print(mat[z][L])
            z-=1
        L+=1
    return

mat = [[1,2,3],[4,5,6],[7,8,9],[11,12,13]]
spiral(mat)

