# problem name : Weird Subtraction Process
# problem link : https://codeforces.com/problemset/problem/946/B
# rating : 1100

a,b=map(int, input().split())
def step1(a,b):
        if a==0 or b==0:
            print(a,b)
            exit()
        else:
            step2(a,b)

def step2(a,b):
    if a>=2*b:
        a=a%(2*b)
        step1(a, b)
    else:
        step3(a,b)

def step3(a,b):
    if b>=2*a:
        b=b%(2*a)
        step1(a, b)
    else:
        print(a,b)
        exit()

while True:
    if a==0 or b==0:
        step1(a, b)
    elif a>=2*b:
        step2(a, b)
    else:
        step3(a, b)