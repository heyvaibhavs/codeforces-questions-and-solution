def toh(N,c1,a,b,c,n):
    if N>0:
        toh(N-1,c1,a,c,b,n)
        print(a,c)
        toh(N-1,c1,b,a,c,n)
print(toh(3,0,1,2,3,4))