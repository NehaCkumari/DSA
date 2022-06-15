#Given an array Arr[] of N integers. 
# Find the contiguous sub-array(containing at least one number) 
# which has the maximum sum and return its sum.
def maxsum(list):
    n=len(list)
    max=[]
    msum=list[0]
    sum=list[0]
    i=1
    while(i<n):
        sum+=list[i]
        if msum<sum:
            msum=sum
        if list[i]<0:
            sum=0
        i+=1
    return msum

l1= [-1,-2,-3]
print(maxsum(l1))

