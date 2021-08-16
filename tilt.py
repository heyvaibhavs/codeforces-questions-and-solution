for _ in range(int(input())):
    n,k1=map(int,input().split())
    a=list(map(int,input().split()))
    if sorted(a)==a:
        print("YES")
        continue
    s=set()
    i,z,c,k=1,0,0,0
    while i<n:
        if a[i]>a[i-1]:
            c+=1
            x=a[i-1]
            y=a[i]
            k+=2
            i+=1
            while i<n:
                if a[i]>a[i-1]:
                    y=a[i]
                    i+=1
                    k+=1
                else:
                    if i==n-1:
                        s2=set()
                        s2.add(a[i-1])
                        if len(s.intersection(s2))==0:
                            s.add(a[i-1])
                        else:
                            z=-1
                    else:
                        i+=1
                    break
            s1=set()
            for j in range(x,y+1):
                s1.add(j)
            if len(s.intersection(s1))==0:
                s=s.union(s1)
                # print(s,s1)
            else:
                z=-1
                break
        else:
            s2=set()
            s2.add(a[i-1])
            if len(s.intersection(s2))==0:
                s.add(a[i-1])
            else:
                z=-1
            i+=1
  #  print(c,k,z)   
    if k1>=c+n-k:
        if z==0:
            print("YES")
        else:
            print("NO")
    else:
        print("NO")
    


