#Recurssive range; sum of all numbers from 0 to n
#6=0+1+2+3+4+5+6

def recrange(num):
    if num==0:
        return 0
    else:
        return num+recrange(num-1)

print(recrange(3))
