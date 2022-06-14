def selection(list):
    n=len(list)
    for i in range(n):
        min=i
        for j in range(i+1, n):
            if list[j]<list[min]:
                min=j
        if min!=i:
            list[i],list[min]=list[min],list[i]
    return list

l1 = [1,3,9,2,5,6]
print(selection(l1))