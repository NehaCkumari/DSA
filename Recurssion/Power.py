#power of a number
#6^3=?

#Brute force
def power(number, pow):
    if pow==0:
        return 1
    elif pow==1:
        return number
    else:
        sum=1
        for i in range(1, pow+1):
            sum=sum*number
        return sum

#recurssion
def powerrec(num, pow):
    if pow==0:
        return 1
    return num*powerrec(num, pow-1)
print(power(6,3))
print(powerrec(6,3))
