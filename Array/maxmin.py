def maxmin(list):
    max=list[0]
    min=list[0]
    n=len(list)
    for i in range(0,n):
        if max<list[i]:
            max=list[i]
        if min>list[i]:
            min=list[i]
    return max, min

l1 =[2,4,1,0,5,9]
print(maxmin(l1))