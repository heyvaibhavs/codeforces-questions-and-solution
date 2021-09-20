for _ in range(int(input())):
    n=int(input())
    for i in range(n):
        j=0
        while j < 2*n:
            if j < i :
                print('(',end="")
                j+=1
            elif j >= 2*n -i:
                print(')',end="")
                j+=1
            else:
                print("()",end="")
                j+=2
        print()




