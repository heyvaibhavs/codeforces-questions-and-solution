# Code by : Sam._.072

s = input()
i, n, z = 0, len(s), 0
while i < n:
    if (i == 0 and s[:4] == 'dot') or (i == n-3 and s[i:i+3] == 'dot'):
        print('dot',end="")
        i += 3
    elif i == 0 and s[:3] == 'at':
        print('at',end="")
        i = 2
    elif  i != 0 and s[i:i+3] == 'dot':
        print('.',end="")
        i += 3
    elif i != 0 and z == 0 and s[i:i+2] == 'at':
        print('@',end="")
        i += 2
        z = -1
    else:
        print(s[i],end="")
        i += 1
