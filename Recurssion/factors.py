#factors of a number
#9=1*3*3; 23=1*23

def factor(num):
    list=[]
    for i in range(1,num+1):
        if num%i==0:
            list.append(i)
    return list

print(factor(5))
