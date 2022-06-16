#Given a matrix of size r*c. Traverse the matrix in spiral form
def spiral(list, row, col):
    last_col=col-1
    last_row=row-1
    r=0
    c=0
    res =[]
    while(r<=last_row and c<=last_col):
        for i in range(c,last_col+1):
            res.append(list[r][i])
        r+=1
        for j in range(r,last_row+1):
            res.append(list[j][last_col])
        last_col-=1
        if last_row>r:
            x=last_col
            while(x>=c):
                res.append(list[last_row][x])
                x-=1
            last_row-=1
        if last_col>c:
            y=last_row
            while(y>=r):
                res.append(list[y][c])
                y-=1
            c+=1
    return res

l1 =[[]]
print(spiral(l1,0,0))




