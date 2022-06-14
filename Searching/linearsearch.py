mylist =[1,5,2,9,34,15]
val=5
def linearsearch(list, val):
    for i in mylist:
        if i==val:
            return True
        else:
            return False

#print(linearsearch(mylist,val))

mlist=[2,5,8,10,24]
def Binarysearch(mylist, val, l, r):
    mid=int((l+r)/2)
    if val==mylist[mid]:
        return True
    elif val<mylist[mid]:
        return Binarysearch(mylist, val, l, mid)
    else:
        return Binarysearch(mylist, val, mid+1, r)

print(Binarysearch(mlist,2, 0,5))






