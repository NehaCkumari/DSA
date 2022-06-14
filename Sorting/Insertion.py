#insertion sort
#list =[12, 11, 13, 5, 6]

def insertion(list):
    n=len(list)
    for i in range(1,n):
        temp=list[i]
        j=i-1
        while j>=0 and list[j]>temp:
            list[j+1]=list[j]
            j-=1
        list[j+1]=temp
    return list


l1 = [1,3,9,2,5,6]
print(insertion(l1))