# this is the templete of stack using linked list with size limit(default size is 10)

class stack:
    def __init__(self,size=10):
        self.maxsize=size   #this is the max size of our stack
        self.list=[]
        self.curr_size=0       # this will tell the current size of the stack

    # this function is used to print the stack 
    def print_stack(self):
        values=[str(self.list[x]) for x in range(self.curr_size-1,-1,-1)]
        return '\n'.join(values)

    # this funtion is for checking the stack is full or not , if it is full then it return True
    #  otherwise it return False
    def isFull(self):
        return self.size==self.maxsize

    # this function check is stack empty or not , if it is empty the return True otherwise return False
    def isEmpty(self):
        return self.list==[]

    # this function return the xurrent size of the stack
    def size(self):
        return self.curr_size

    # this function is used to push an element in the stack
    def push(self,value):
        if self.isFull():
            return -1
        self.list.append(value)
        self.curr_size+=1

    # this function is used to pop an element from from stcak
    def pop(self):
        if self.isEmpty():
            return -1
        self.curr_size-=1
        return self.list.pop()

    #  this function return the top element of the stack
    def peek(self):
        if self.isEmpty():
            return -1
        return self.list[-1]

    # this function delete the whole stack
    def delete(self):
        self.list=None

if __name__ == '__main__':
    s=input()
    obj=stack(len(s))
    s1,n="",len(s)
    for i in range(n):
        if s[i]=='.':
            while obj.isEmpty()!=True:
                s1+=obj.pop()
            if s[i]=='.':
                s1+='.'
        else:
            obj.push(s[i])
    while obj.isEmpty()!=True:
        s1+=obj.pop()
    print(s1)
    



    
