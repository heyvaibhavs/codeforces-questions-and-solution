# Code by : Sam._.072

n = int(input())
d = dict()
for i in range(n):
    s = input()
    if d.get(s,False) == False:
        d[s] = 1
        print("ok")
    else:
        print(s+str(d[s]))
        d[s] += 1
        