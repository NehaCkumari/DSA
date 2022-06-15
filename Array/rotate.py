#Given an array, rotate the array by one position in clock-wise direction.
def rotate(list, pos):
    n=len(list)
    if pos>=n:
        pos=pos-n
    for i in range(pos):
        temp=list[n-1]
        for j in range(n-1):
            list[n-1-j]=list[n-2-j]
        list[0]=temp
    return list

l1= [1,2,3,4,5]
print(rotate(l1,6))

