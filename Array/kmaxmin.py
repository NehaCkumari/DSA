#Given an array arr[] and an integer K 
# where K is smaller than size of array, 
# the task is to find the Kth smallest element in the given array. 
# It is given that all array elements are distinct.
def sort(list):
    n=len(list)
    
    
    for i in range(1,n):
        j=i-1
        key=list[i]
        while key<list[j] and j>=0:
            list[j+1]=list[j]
            j-=1
        list[j+1]=key
    return list

def kmaxmin(list, k):
    sort(list)
    if k-1<=len(list):
        min=list[k-1]
    if len(list)-k>=0:
        max=list[len(list)-k]
    return max, min

l1= [7,10,4,3,20,15] #[3,4,7,10,15,20]
print(kmaxmin(l1,3))
print(sort(l1))



