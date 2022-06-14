#Decimal to binary
#13=1101

def dectobin(num):
    q=num
    list1=[]
    while (q!=0):
        q=q/2
        list1.append(q%2)
    list1.reverse
    return list1

print(dectobin(13))