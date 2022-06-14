#product of an array
#[1,2,3,4]=24
#recurssion

def prodarr(arr, n):
    if n==1:
        return arr[0]
    else:
        return arr[n-1]*prodarr(arr, n-1)

print(prodarr([1,2,3,4],4))