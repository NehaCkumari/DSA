#Given an array (or string), the task is to reverse the array/string.
#3/2=1.5? and 3%2=1(remender)

def reverse(list):
    n=len(list)
    for i in range(0,int(n/2)):
        list[i],list[n-1-i]=list[n-1-i],list[i]
    return list

l1=[1,2,3,4,5]
l2=[1,2,3,4]
print(reverse(l1))
print(reverse(l2))


    