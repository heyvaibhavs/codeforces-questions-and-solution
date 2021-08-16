class Node:
    def __init__(self,value=None):
        self.value = value
        self.next = None
# defining linked list class
class LinkedList:
    def __init__(self):
        self.head=None
    
    def __iter__(self):
        node=self.head
        while node:
            yield node
            node=node.next

# defining stack class which contains all stacks functions
class Stack:
    def __init__(self):
        self.obj=LinkedList()
        self.curr_size=0
    
    # this function return True if stcak is empty otherwise it return False
    def isEmpty(self):
        return self.obj.head==None

    # this function push an element on the stack
    def push(self,value):
        newnode=Node(value)
        self.curr_size+=1
        newnode.next=self.obj.head
        self.obj.head=newnode
    
    # this function pop an element from the stack
    def pop(self):
        if self.isEmpty():
            return -1
        self.curr_size-=1
        nodevalue=self.obj.head.value
        self.obj.head=self.obj.head.next
        return nodevalue
    
    # this function return the top element of the stack
    def peek(self):
        if self.isEmpty():
            return -1

    
    # this function return the current size of the stack
    def size(self):
        return self.curr_size

    def index(self,value):
        temp,i=self.obj.head,1
        while temp:
            # print(temp.value)
            if temp.value<value:
                return i
            i+=1
            temp=temp.next
        return -1


if __name__=='__main__':
    for _ in range(int(input())):
        n=int(input())
        a=list(map(int,input().split()))
        obj=Stack()
        for i in range(n-1,-1,-1):
            obj.push(a[i])
        for i in range(n-1):
            t=obj.index(obj.pop())
            if t!=-1:
                print(t+i+1,end=" ")
            else:
                print(-1,end=" ")
        print(-1,end=" ")
        print()
        
    
    
    
    