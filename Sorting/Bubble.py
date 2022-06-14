def bubble(list):
    n=len(list)
    for i in range(n):
        flag=0
        for j in range(0, n-1-i):
            if list[j]>list[j+1]:
                list[j], list[j+1]=list[j+1], list[j]
                flag=1
        if flag==0:
            break
    return list

l1= [2,1,7,4,9,0]
print(bubble(l1))
