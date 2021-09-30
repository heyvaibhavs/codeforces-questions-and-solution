# problem name : Mocha and Hiking
# problem link : https://codeforces.com/problemset/problem/1559/C
# Rating : 1200

class Edge:
    def __init__(self,v1,v2):
        self.v1=v1
        self.v2=v2
def getParent(v,parent):
    if parent[v]==v:
        return v
    return getParent(parent[v], parent)

def kruskal(edge,n):
    parent=[i for i in range(n)]
    count=0
    i=0
    output=[]
    while count<n-1:
        curredge= edge[i]
        p1=getParent(curredge.v1,parent)
        p2=getParent(curredge.v2,parent)
        if p1!=p2:
            output.append(curredge)
            count+=1
            parent[p1]=p2
        i+=1
    return output
    
if __name__=='__main__':
    for _ in range(int(input())):
        n=int(input())
        e=[]
        a=list(map(int, input().split()))
        for i in range(n):
            if i!=n-1:
                e.append(Edge(i,i+1))
            if a[i]==0:
                e.append(Edge(i, n))
            elif a[i]==1:
                e.append(Edge(n, i))
        op=kruskal(e, n+1)
        s=set()
        for i in op:
            print(i.v1,i.v2)
            s.add(i.v1)
            s.add(i.v2)
        for i in s:
            print(i+1,end=" ")
        print()


        
        