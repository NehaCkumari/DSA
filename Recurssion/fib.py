#fibonacci series
#0,1,1,2,3,5,..
def fib(num):
    if num==0:
        return 0
    elif num==1:
        return 1
    else:
        return fib(num-1)+fib(num-2)

print(fib(4))