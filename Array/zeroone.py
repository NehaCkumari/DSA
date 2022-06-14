#Given an array of size N containing only 0s, 1s, and 2s; sort the array in ascending order.
def sorting(list):
    l0=[]
    l1=[]
    l2=[]
    n=len(list)
    for i in range(n):
        if list[i]==0:
            l0.append(0)
        elif list[i]==1:
            l1.append(1)
        else:
            l2.append(2)
    l0.extend(l1)
    l0.extend(l2)
    return l0

l=[0,1,2,1,0,2,0,1]
print(sorting(l))
