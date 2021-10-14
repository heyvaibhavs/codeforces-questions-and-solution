# Code by : Sam._.072\

class A:
    def test1(self):
        print("a")
class B(A):
    def test(self):
        print("b")
class C(A):
    def test(self):
        print("c")
class D(B,C):
    def test2(self):
        print("d")
obj=D()
obj.test()


