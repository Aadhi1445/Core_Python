'''Spuer() using instance Method'''
# class A:
#     def m1(self):
#         print("A class")
# class B(A):
#     def m1(self):
#         print('B class')
#         super().m1()
# class C(A):
#     def m1(self):
#         print('C class')
#         super().m1()
# class E:
#     def f(self):
#         print('E class')
# class F(E):
#     def e(self):
#         print('F class')
# class D(B,C,F):
#     def m1(self):
#         print('D class')
#         super().m1()
# print(D.mro())
# c1=C()
# c1.m1()
# print(C.mro())
# print(B.mro())
# print(A.mro())

'''Super() using Classmethod'''
# class A:
#     @classmethod
#     def m1(cls):
#         print("A class")
# class B(A):
#     @classmethod
#     def m1(cls):
#         print('B class')
#         super().m1()
# class C(A):
#     @classmethod
#     def m1(self):
#         print('C class')
#         super().m1()
# class D(B,C):
#     @classmethod
#     def m1(self):
#         print('D class')
#         super().m1()
# d1=D()
# print(D.mro())
# d1.m1()
# c1=C()
# c1.m1()
# print(C.mro())
# print(B.mro())
# print(A.mro())

class A:
    @classmethod
    def cm(cls):
        print('A Class Method')
class B(A):
    def im(self):
        super().cm()
        print('B Instance method')
    @classmethod
    def cm(cls):
        super().cm()
        print('B class method ')
b1=B()
b1.im()
b1.cm()