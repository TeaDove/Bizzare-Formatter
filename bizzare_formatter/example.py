class A:
    def test(self):
        print("A")

class B(A):
    def test(self):
        print("B")
        super().test()

class C(A):
    def test(self):
        print("C")

class D(B, C):
    def new_test(self):
        print("D")

obj = D()
print(D.mro())
obj.test()