for _ in range(int(input())):
    n=int(input())
    s=input()
    c=0
    for i in s:
        i= int(i)
        if i >0:
            c+= i + 1
    # print(c)
    if s[-1]!='0':
        c -=1
    print(c)    