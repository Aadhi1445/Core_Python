# class User:
#     def __init__(self,n,a,g,dob):
#         self.name=n
#         self.age=a
#         self.gender=g
#         self.dob=dob
#     def login(self):
#         print('Successfully Logged in')
#     def logout(self):
#         print('successfully logged out')
# print(User.mro())
# class Instagram(User):
#     def post(self):
#         print(f'{self.name} post')
#         print('got 1l likes')
# a1=Instagram('parul',15,'Male','23-07-2004')
# a1.post()
# a1.login()
# a1.logout()
# print(Instagram.mro())
# print('-'*50)
# class Restaurants:
#     def __next__(self,n,r,add):
#         self.name=n
#         self.rating=r
#         self.address=add
#     def display_menu(self):
#         print('All Dishes are non-veg only')
# class Swiggy(User,Restaurants):
#     def display(self):
#         print(f'Name:{self.name}\n'
#               f'Age:{self.age}\n'
#               f'Gender:{self.gender}\n'
#               f'Dob:{self.dob}')
#     def display(self):
#         print('user"s details')
# print(Swiggy.mro())
# class Zomato(User,Restaurants):
#     def display(self):
#         print('Zomato')
# print(Zomato.mro())
# class Customer(Swiggy,Zomato):
#     def order(self):
#         print('Just Ordered')
# c1=Swiggy('Parul',35,'Male','23-07-2004')
# c1.display()
# print(Customer.mro())
# print('-'*50)
# class Bank(User):
#     Name='RBI'
#     def guide_lines(self):
#         print('Beware of Scammer and Call 0004')
# class Bhim_UPI(Bank,Swiggy):
#     def Payments(self,amount):
#         print(f'{self.amount} has been paid through UPI')
# b1=Bhim_UPI('Shiva',21,'male','11-09-2004')
# b1.display()
# print(Bhim_UPI.mro())
# print('-'*50)
#
'''Super using in Single Inheritance'''
# class A:
#     def __init__(self,n):
#         self.name=n
# class B(A):
#     def __init__(self,n,m):
#         self.marks=m
#         super().__init__(n)
# b1=B('Aadhya',45)
# print(b1.name)
'''Super() using in multilevel inheritance'''
# class A:
#     def __init__(self,n):
#         print('A Constructor Called')
#         self.name=n
#         print('name:',self.name)
# class B(A):
#     def __init__(self,n,m):
#         print('B Constructor Called')
#         self.marks=m
#         print('marks:',self.marks)
#         super().__init__(n)
# class C(B):
#     def __init__(self,n,a,m):
#         print('C Constructor Called')
#         self.age=a
#         print('age:',self.age)
#         super().__init__(n,m)
# class D(C):
#     def __init__(self,n,m,a,g):
#         print('D Constructor Called')
#         self.gender=g
#         print('gender:',self.gender)
#         super().__init__(n,a,m)
# print(D.mro())
# d1=D('Aadhya',45,22,'M')
'''Super using in Multiple Inheritance'''
# class A:
#     def __init__(self,n,m):
#         print('A class Constructor')
#         self.name=n
#         super().__init__(m)
# class B:
#     def __init__(self,m):
#         print('B class Inheritance')
#         self.marks=m
# class C(A,B):
#     def __init__(self,a,n,m):
#         print('C class Constructor')
#         self.age=a
#         super().__init__(n,m)
# print(C.mro())
# c1=C(22,'Aadhya',456)
'''Super using in Hierarchical Inheritance'''
# class A:
#     def __init__(self,n,a):
#         self.name=n
#         super().__init__(a)
# class B:
#     def __init__(self,a):
#         self.age=a
# class C(A,B):
#     def __init__(self,n,m,a):
#         self.marks=m
#         super().__init__(n,a)
#     def display(self):
#         print(f'{self.name} '
#               f'{self.age} '
#               f'{self.marks}')
# c1=C('Aadhya',456,22)
# c1.display()

'''Super using Hybrid Inheritance'''
# class A:
#     def __init__(self,n):
#         self.name=n
#     def display(self):
#         print(f'{self.name} ')
# class B(A):
#     def __init__(self,n,a,b):
#         self.branch=b
#         super().__init__(n,a)
#     def display(self):
#         print(f'{self.name} '
#               f'{self.age} '
#               f'{self.branch}')
# class C(A):
#     def __init__(self,n,a):
#         self.age=a
#         super().__init__(n)
#     def display(self):
#         print(f'{self.name} '
#               f'{self.age} ')
# class D(B,C):
#     def __init__(self,n,a,b,g):
#         self.gender=g
#         super().__init__(n,a,b)
#     def display(self):
#         print(f'{self.name} '
#               f'{self.age} '
#               f'{self.gender} '
#               f'{self.branch}')
# print(D.mro())
# d1=D('Aadhya',22,'EEE','M')
# d1.display()
# b1=B()
# b1.display()
# c1=C()
# c1.display()
# a1=A()
# a1.display()

l=[1,2,[4,5],6]
print(l[2][1])