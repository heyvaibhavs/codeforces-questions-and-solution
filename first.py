def isprime(n):
    if n==2:
        return True
    if n==1:
        return False
    i=2
    while i*i<n:
        if n%i==0:
            return False
        i+=1
    return True

a=[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
for i in a:
    print(i-1+i,":",isprime(i-1+i),"   i=",i,"   ",i+1+i,":",isprime(i+1+i))