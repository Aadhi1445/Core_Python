# # class Ticket:
# #     source="Rjy"   '''object dictionary frmt lo store avthaiii'''
# #     Destination="hyd"
# #     total=0
# #     # print("total=",total)
# #     def __init__(abc,name,age,gender):
# #         '''name,age,gender --- instance variables '''
# #         abc.name=name
# #         abc.age=age
# #         abc.gender=gender
# #         Ticket.total += 1
# #     def __str__(abc):
# #         return abc.source
# #     def greet(abc):
# #         print("hello", abc.name)
# # t1 = Ticket("Parul",54,"M")
# # t1.greet()
# # s=t1
# # Ticket.source="kkd"
# # t1.name="mr_Aasish"
# # t1.age=16
# # # print(s)
# # print(t1.name)
# # print(t1)
# # print(t1.source)
# # print(t1.Destination)
# # print(t1.total)
# # print("age=",t1.age)
# # t2=Ticket("gajini",12,"N")
# # print(t1.source)
# # print(t1.Destination)
# # print(t1.total)
# from stringprep import b1_set
#
#
# # #Q1
# # class Student:
# #     def __init__(self,name,marks):
# #         self.name=name
# #         self.marks=marks
# #     def is_passed(self ):
# #         if self.marks>40:
# #             print("Pass")
# #         else:
# #             print("Fail")
# #
# # s1=Student("parul",65)
# # s1.is_passed()
# # s2=Student("jai",30)
# # s2.is_passed()
#
#
# # # Q2
# # class employee:
# #     name="Parul"
# #     company_name="TechCorp"
# #     def __init__(self,name,company_name):
# #         self.name=name
# #         self.company_name=company_name
# #     @classmethod
# #     def update(cls,companyname,name):
# #         cls.company_name=companyname
# #         cls.name=name
# # # a=employee("shiva","Tech")
# # # print(a.name)
# # # print(a.company_name)
# # b=employee("apple","shiva")
# # print(b.name)
# # print(b.company_name)
#
#
# # e1=employee()
# # e1.update("Adhya","mahindra_Thar")
# # print(employee.company_name,employee.name)
# # print(employee.name)
# # employee.update()
#
# # Q4
# # class Car:
# #     wheels=4
# #     def __init__(self,mileage):
# #         self.mileage=mileage
# #     @classmethod
# #     def update(cls,n_wheels):
# #         cls.wheels=n_wheels
# #     def display_specs(self):
# #         print(self.mileage,"-",self.wheels)
# # c1=Car(45)
# # c1.display_specs()
# # '''Car.display_specs(c1)'''
# # print("after changing")
# # Car.update(8)
# # c1.display_specs()
# # # c1.update(7)
# # # Car.display_specs(c1)
# # print(Car.__name__)
# # print(Car.__doc__)
# # print(Car.__dict__)
# # print(Car.__annotations__)
#
# # # Q3
# # class MathsOps:
# #     # def __init__(self,num):
# #     #     self.num=num
# #     @staticmethod
# #     def is_even(x):
# #         print(x%2==0)
# # m1=MathsOps()
# # m1.is_even(5)
# # # MathsOps.is_even(4)
# # # MathsOps.is_even(5)
# #Q5
# class Temp:
#     def __init__(self,celsius):
#         self.celsius=celsius
#     @staticmethod
#     def to_Fahrenheit():
#         return (t1.celsius*9//5)+32
#
#     def show_conversion(self):
#         print(f"{self.celsius} -- {Temp.to_Fahrenheit()}")
# t1=Temp(10)
# Temp.to_Fahrenheit()
# # t1.to_Fahrenheit(10)
# t1.show_conversion()
#
# # Q6
# # class Book:
# #     total_books=0
# #     def __init__(self,title,author):
# #
# #         self.title=Book.is_valid_title(title)
# #         self.author=author
# #         Book.total_books=Book.total_books+1
# #     @classmethod
# #     def from_string(cls,book_str):
# #         title,author=book_str.split("-")
# #         return cls(title,author)
# #
# #     @staticmethod
# #     def is_valid_title(title):
# #         if len(title)>=3:
# #             return title
# #         else:
# #             return "Invalid Title"
# # b1=Book.from_string("Ada-zxcv")
# # print(b1.title)
# # print(b1.author)
# # print(b1.total_books)
# # b1=Book.from_string("Aa-zxcv")
# # print(b1.title)
# # print(b1.author)
# # print(b1.total_books)
#
# # Q7
# class Employee:
#     bonus_rate=0.1
#     def __init__(self,name,base_salary):
#         self.name=name
#         self.base_salary=base_salary
#     def final_salary(self):
#         return (self.base_salary+(self.base_salary * Employee.bonus_rate))
#     @staticmethod
#     def is_valid_salary(base_salary):
#       return base_salary>0
#     @classmethod
#     def update_bonus(cls,new_rate):
#         Employee.bonus_rate=new_rate
#         return Employee.bonus_rate
# # e1=Employee("James",100)
# # print(e1.final_salary())
# # e2=Employee("asd",6)
# # print(e2.final_salary())
# bonus_rate=Employee.update_bonus(2)
# # print(bonus_rate)
# # e1=Employee("James",100)
# # print(e1.final_salary())
# # e2=Employee("asd",6)
# # print(e2.final_salary())
# e3=Employee("asd",0)
# # print(e3.base_salary)
# print(e3.final_salary())

# # Q8
# class Course:
#     total_students=0
#     def __init__(self,name,age):
#         self.s_name=name
#         self.age=age
#         self.enroll()
#     def enroll(self):
#         Course.total_students+=1
#     @classmethod
#     def show_total(cls):
#         print(Course.total_students)
#     @staticmethod
#     def is_eligible(age):
#             return True if age>=18 else False
# # s1=Course("Aadhya",25)
# # print(s1.age)
# # print(s1.is_eligible(s1.age))
#
# # Course.show_total()
# # s2=Course("shiv",16)
# # print(s2.is_eligible(s2.age))
# # print(s2.age)

# # Q9
# class Bank_Acc:
#     bank_name="RBI"
#     def __init__(self,name,balance=0):
#         self.holder=name
#         self.balance=balance
#     def deposit(self,amount):
#         # if amount==True:
#         self.balance+=amount
#         return self.balance
#     @classmethod
#     def c_b_name(cls,n_name):
#         Bank_Acc.bank_name=n_name
#     @staticmethod
#     def v_amount(amount):
#         if amount>0:
#             return amount
#     def display(self):
#         print(self.holder,self.balance,Bank_Acc.bank_name)
# c1=Bank_Acc("aadhya")
# # c1.display()
# # c1.deposit(c1.v_amount(100))
# # print(c1.balance)
# c1.deposit(c1.v_amount(0))
# print(c1.balance)
# # c1.display()

# # Q10
# class Student:
#     passing_marks=40
#     def __init__(self,name,marks):
#         self.name=name
#         self.marks=marks
#     def result(self):
#         if self.marks>Student.passing_marks:
#             print("Pass")
#             return "Pass"
#         else:
#             print("Fail")
#             return "Fail"
#     @classmethod
#     def update_passing_marks(cls,n_marks):
#         cls.passing_marks=n_marks
#     @staticmethod
#     def grade_category(marks):
#         if marks>=80:
#             return "A"
#         elif marks>=70:
#             return "B"
#         elif marks>=60:
#             return "C"
#         elif marks>=50:
#             return "D"
#         elif marks>=40:
#             return "E"
#         else:
#             return "Fail"
#     def display(self):
#         print(self.name,self.marks,self.result(),self.grade_category(self.marks))
# s1=Student("James",85)
# s1.display()
# # Student.update_passing_marks(50)
# # print(Student.passing_marks)



























































