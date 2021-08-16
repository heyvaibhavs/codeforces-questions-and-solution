def sepratenumber(s):
    if len(s)==1:
        print("no")
        return
    else:
        for i in range(1, len(s)//2 + 1):
            genstr=s[:i]
            prev = int(genstr)
            
            while len(genstr) < len(s):
                next =prev +1
                genstr = genstr +str(next)
                prev= next
                
            if genstr == s:
                print("yes" , s[:i])
                return
        print("no")
 
s=input()
sepratenumber(s)