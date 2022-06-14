#sum of digits of the positive numbers using recurssion
#sum(1233)=1+2+3+3=?
#Recurssion
    #Step 1: simiar subproblem
    #Step 2: base case; to stop recurssion
    #Step 3: Unintensional case

#Brute force
def SumOfDigits(number):
    n=number
    sum=0
    while(n!=0): #while(true) countinue else return
        sum+=int(n%10)
        n=int(n/10)
    return sum

#Recurssion
def SumDigits(number):
    if number==0:
        return 0
    return int(number%10)+SumDigits(int(number/10))
print(SumOfDigits(12))
print(SumDigits(0))
    