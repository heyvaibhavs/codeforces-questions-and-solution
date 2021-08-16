class treeNode:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def diif_level(root,d):
    global c
    if root is None:
        return 
    if d%2==0:
        c+=root.data
    else:
        c-=root.data
    print(c)
    diif_level(root.left,d+1)
    diif_level(root.right,d+1)
    return c

if __name__ == '__main__':
    root=treeNode(1)
    root1=treeNode(2)
    root2=treeNode(3)
    root.left=root1
    root.right=root2
    print(diif_level(root,0))