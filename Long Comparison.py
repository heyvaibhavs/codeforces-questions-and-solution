# Code by : Sam._.072

for _ in range(int(input())):
    x1, l1 = map(int, input().split())
    x2, l2 = map(int, input().split())
    s1, s2 = str(x1), str(x2)
    if len(s1)+l1 > len(s2)+l2:
        print('>')
    elif len(s1)+l1 < len(s2)+l2:
        print('<')
    else:
        if len(s1)<len(s2):
            x1 = x1*(10**abs(len(s1)-len(s2)))
        elif len(s1)>len(s2):
            x2 = x2*(10**abs(len(s1)-len(s2)))
        if x1 > x2:
            print('>')
        elif x1 < x2:
            print('<')
        else:
            print('=')
        


        