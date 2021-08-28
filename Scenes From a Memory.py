import math
def prime(n):
    if n%2==0:
        return True
    for i in range(3,int(math.sqrt(n)+1)):
        if n%i==0:
            return True
    return False
for _ in range(int(input())):
    k=int(input())
    s=input()
    f=10*[0]
    for i in s:
        f[ord(i)-48]+=1
    if f[1]>0:
        print(1)
        print(1)
    elif f[4]>0 :
        print(1)
        print(4)
    elif f[6]>0 :
        print(1)
        print(6)
    elif f[8]>0 :
        print(1)
        print(8)
    elif f[9]>0 :
        print(1)
        print(9)
    elif f[2]>1 :
        print(2)
        print(22)
    elif f[3]>1 :
        print(2)
        print(33)
    elif f[5]>1 :
        print(2)
        print(55)
    elif f[7]>1 :
        print(2)
        print(77)
    else:
        z=0
        for i in range(1,10):
            for j in range(1,10):
                if f[i]>0 and f[j]>0 and (s.index(str(i))<s.index(str(j)) or s.index(str(i))<s.rindex(str(j)) ) :
                    n1=i*10+j
                    # print(n1)
                    if i==j and f[i]<2:
                        continue
                    else:

                        if prime(n1):
                            print(2)
                            print(n1)
                            z=-1
                            break
                if z==-1:
                    break
   
    
    

