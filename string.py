
def funny(s):
    t=s[-1:-len(s)]
    a={}
    b={}
    for i in range(len(s)-2):
        a[i]=ord(s[i])
        b[i]=ord(t[i])
        if a[i]!=b[i] or a[i]!=-1*b[i]:
            c=-1
            return "Not Funny"
    if c!=-1:
        return "Funny"
s="acxz"
print(funny(s))    
    