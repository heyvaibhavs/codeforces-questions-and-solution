'''
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
'''

# Write your code here
inp = input("input")
x=0
for i in inp:
    if i!='G' and i!='C' and i!='T' and i!='A':
        x=-1
        break
if(x!=-1):
    for j in inp:        
        if(j=='G'):
            print("C")
        elif(j=='C'):
            print('G')
        elif(j=='T'):
            print('A')
        else:
            print('U')
else:
    print("invalid input")