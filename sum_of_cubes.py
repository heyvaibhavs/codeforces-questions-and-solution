for _ in range(int(input())):
    x=int(input())
    i,z=1,0
    while x-i**3>0:
        t=pow(x-i**3,1./3.)
        if i==5779 or i==7993:
            print("t=",t,(i**3)+(x-i**3))
        if t-int(t)==0 :
            z=-1
            break
        i+=1
    print(i,x-i**3)
    if z==-1:
        print("YES")
    else:
        print("NO")




