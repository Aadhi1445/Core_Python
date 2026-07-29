"""Arthmetic Methods"""
# # class Student:
# #     def __init__(self,marks):
# #         self.marks=marks
# # s1=Student(45)
# # s2=Student(12)
# # # print(s1.marks+s2.marks)
# # # print(s1+s2)
# class Student:
#     def __init__(self,marks):
#         self.marks=marks
#         # print(self.marks)
#     def __add__(self,z):
#         k=self.marks+z.marks
#        return Student(k)
#     def __str__(self):
#         print("add:",end="")
#         return f"{self.marks}"
# #     def __sub__(self, z):
# #         print("sub:", end="")
# #         return self.marks-z.marks
# #     def __mul__(self,z):
# #         print("mul:", end="")
# #         return self.marks*z.marks
# #     def __mod__(self,z):
# #         print("mod:", end="")
# #         return self.marks % z.marks
# #     def __truediv__(self, z):
# #         print("truediv:", end="")
# #         return self.marks / z.marks
# #     def __floordiv__(self, z):
# #         print("floordiv:", end="")
# #         return self.marks // self.marks
# s1=Student(10)
# s2=Student(2)
# s3=Student(4)
# print(s1+s2+s3)
# # print(s1/s2)
# # print(s1 // s2)
# # print(s1-s2)
# # print(s1*s2)
# # print(s1%s2)
# # # # '''s1.__add__(s2)'''

# """__str__"""
# class Industry:
#     def __init__(self,name,dept,salary):
#         self.name=name
#         self.dept=dept
#         self.salary=salary
# e1=Industry("parul","labour",250)
# print(e1)
class Industry:
    def __init__(self,name,dept,salary=0):
        self.name=name
        self.dept=dept
        self.salary=salary
    def __str__(self):
        return f" '{self.name}' belongs to '{self.dept}'department and his is  salary: '{self.salary}'"
    def __repr__(self):
        return self.name
e1=Industry("Parul","manager")
print(e1)
e2=Industry("sathwik","hr",20000)
print(e2)
l=[e1,e2]
print(l)
#
# '''__repr__'''
# class Bank:
#     def __init__(self,name,acc_no,balance=0,):
#         self.name=name
#         self.acc_no=acc_no
#         self.balance=balance
#     def __repr__(self):
#         return f"Name: {self.name} \n account_no: {self.acc_no} \n balance:{self.balance}"
#     def __str__(z):
#         return f" Account_number:{z.acc_no} belongs to ' {z.name} ' his balance :{z.balance}"
# c1=Bank("Parul",100025463)
# # c2=Bank("sathwik",100056437,500)
# # print(c1)
# print(c1)
# print(repr(c1))
#
# '''relational operators'''
# class Student:
#     def __init__(self,n,id,m):
#         self.marks=m
#         self.id=id
#         self.name=n
#
#     def __gt__(self, z):
#         return self.marks < z.marks and self.marks <= z.marks
#
#     def __gt__(self, z):
#         print("hi")
#         return self.marks > z.marks
#
#     def __gt__(self, z):
#         return self.marks < z.marks and self.marks <= z.marks
#     def __ge__(self,z):
#         return self.marks>= z.marks
#     def __le__(self, other):
#         return self.marks<=other.marks
#     def __lt__(self, other):
#         return self.marks<other.marks
#
# s1=Student("adhya",1,23)
# s2=Student("paru",2,78)
# print(s1>s2)
# print(s1>=s2)
# print(s1<s2)
# print(s1<=s2)
# '''len'''
# class Student:
#     def __init__(self,n):
#         self.name=n
#     def __len__(self):
#         return len(self.name)
#         # return 20+40
# s1=Student('Aadhya')
# print(len(s1))
# '''contain'''
# class School:
#     # l=[ ]
#     def __init__(self,name):
#         self.name=name
#         # School.l.append(self.name)
#     def __contains__(self,z):
#         return z in self.name
# s1=School('Aadhya')
# s2=School('kiran')
# s3=School('parul')
# # print(s1.name in School.l)
# print(s1 in School)

# n=int(input())
# m=int(input())
# for i in range(n-1,0,-1):
#     if str(m) in str(i):
#         print(i)
#         break









