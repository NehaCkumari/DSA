#Greatest common divisor
#(1,2)=1; (2,4)=2; (6,9)=3;

#Brute Force
def factor(num):
    list=[]
    for i in range(1,num+1):
        if num%i==0:
            list.append(i)
    return list

def GCD(num1, num2):
    list1=factor(num1)
    list2=factor(num2)
    common=1
    for i in range(1,len(list1)):
        for j in range(1,len(list2)):
            if list1[i]==list2[j]:
                common=list1[i]
    return common

print(GCD(23,8))
#Recurssion
def GCDrec(num1, num2):
    if num2==0:
        return num1
    return GCDrec(num2, num1%num2)

print(GCDrec(4,8))