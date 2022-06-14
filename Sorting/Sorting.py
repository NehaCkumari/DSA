mylist=[2,5,1,36,23,15,9]
def selectionsort(mylist):
    #fpoint,tpoint,min
    j=0
    for j in range(len(mylist)):
        min=mylist[j]
        for i in range(j+1,len(mylist)):
            if mylist[i]<min:
                min=mylist[i]
                k=i
        mylist[j], mylist[k]=mylist[k], mylist[j]
    return mylist

print(mylist)
print("Selection Sorted array")
print(selectionsort(mylist))

def Bubblesort(mylist):
    for i in range(len(mylist)):
        for j in range(len(mylist)-1-i):
            if mylist[j]>mylist[j+1]:
                mylist[j], mylist[j+1]=mylist[j+1],mylist[j]
    return mylist

print("Bubble Sorted array")
print(Bubblesort(mylist))




