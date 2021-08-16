def calculate (arr, n) : 
    c=0
    arr.sort()
    t=arr[0]
    x=1
    for i in range(1,n):
        if arr[i]==t:
            x+=1
        else:
            if x>1:
                c=c+x*(x-1)//2
            t=arr[i]
            x=1
        
    if x>1:
        c=c+x*(x-1)//2
    return c

arr=[1,3,1,4,4]
print(calculate(arr,5))