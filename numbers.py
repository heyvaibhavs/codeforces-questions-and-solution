def numbers(n):
    s=""
    r=0
    while(n>=3):
        if n%3==0:
            for i in range(n):
                s=s+'5'
                n=n-1    
        elif n%5==0 and n%3!=0:
            for i in range(n):
                if n%3!=0:
                    n=n-5
                    r=r+5
                else:
                    break
            for i in range(n):
                s=s+'5'
                n=n-1
        elif n%5==0:
            for i in range(n):
                s=s+'3'
                n=n-1
        else:
            r=r+5
            n=n-5
    if r%5==0 and n==0:
        for i in range(r):
            s=s+'3'
       
    if len(s)>=3:
        return s
    else:
        return -1
for i in range(1,11):
    print(numbers(i))
            