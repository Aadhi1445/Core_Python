# '''• Create a class Person whose constructor takes age as an argument.
#     Raise a ValueError if the age is less than 0.'''
# class Person:
#     def __init__(self,age):
#         if age>0:
#             self.age=age
#         else:
#             raise ValueError('"Age cannot be zero"')
# p1=Person(0)
''' • Write a function named find_length(obj) that uses a loop
    to calculate the length of the given object without using the built-in len() function.
    The function should return the calculated length if the object is iterable.
    If a non-iterable object such as an integer is passed,
    the function should raise and handle a TypeError,
    and print an appropriate error message explaining what happens when an integer is sent as input. '''
def find_length(obj):
    if isinstance(obj,(list,str,tuple,set)):
        c=0
        for i in obj:
            c+=1
            





# def find_length(obj):
#     try :
#         c=0
#         for i in (obj):
#             c+=1
#         return c
#     except TypeError:
#         raise TypeError('Integer Object Cannot be Iterated')
# print(find_length([1,2,3,4]))
# print(find_length(0))
# '''• Create a class Student with an attribute marks.
#     Implement a method set_marks(marks) that raises a ValueError
#         if marks are not in the range 0 to 100. '''
# class Student:
#     def __init__(self,marks):
#         # if 0<=marks<=100:
#         self.marks=marks
#         # else:
#         #     raise ValueError('Marks Should be in 0 to 100 range ')
#     def set_marks(self,marks):
#         if 0<=marks<=100:
#             self.marks = marks
#         else:
#             raise ValueError('Marks Should be in 0 to 100 range ')
# s1=Student(111)
# s1.set_marks(111)
# '''• Create a custom exception named InvalidAgeError.
#     Create a class Voter with a method check_eligibility(age) that raises this exception if age is less than 18.'''
# class InvalidAgeError(Exception):
#     pass
# class Voter:
#     def check_availability(self,age):
#         if age<18:
#             raise InvalidAgeError('Age should  greater than 18')
# v1=Voter()
# v1.check_availability(15)
# '''• Create a class BankAccount with an attribute balance.
#     Implement a method withdraw(amount) that raises an exception
#     if the withdrawal amount is greater than the available balance.'''
# class InvalidAmount(Exception):
#     pass
# class BankAccount:
#     def __init__(self,balance):
#         self.balance=balance
#     def withdraw(self,amount):
#         if amount>self.balance:
#             raise InvalidAmount('Insufficient Funds ')
# a1=BankAccount(5000)
# a1.withdraw(5500)
# '''• Create a class PasswordValidator with a method validate(password).
#     Raise an exception if the password length is less than 8 characters. '''
# class PasswordError(Exception):
#     pass
# class PasswordValidator:
#     def validate(self,password):
#         if len(password)<8:
#             raise PasswordError('Password length should be above 8 Characters')
# p=PasswordValidator()
# # p.validate('asdfg')
# p.validate('asdfgjklo')
'''• Create a class UserInput with a method get_integer(value). 
    Handle ValueError and TypeError using separate except blocks.'''
# class UserInput:
#
#         def get_integer(self,value):
#             try:
#                 return int(value)
#             except ValueError as e:
#                 print(e)
#             except TypeError as e:
#                 print(e)
#             finally:
#                 print("adii babu")
# u = UserInput()
# u.get_integer("")


# '''• Create a base class Shape with a method area() that raises NotImplementedError.
#     Create a child class Rectangle that overrides and implements the area method.'''
# # class NotImplementedError(Exception):
# #     pass
# class Shape:
#     def area(self):
#         raise NotImplementedError('Method Not Implemented')
# class Rectangle(Shape):
#     def area(self):
#         print('Area')
# r1=Rectangle()
# r1.area()
# Shape().area()

# ''' • Create a class Service with a method that calls another method which raises an exception.
#     Catch and handle the exception in the Service class.'''
# class Service:
#     def method(self):
#         self.e_method()
#     def e_method(self):
#         raise NotImplementedError('Exception')
# Service().method()

''' • Create a class Transaction with a method process() 
    that uses try, except, and finally blocks to ensure a cleanup message is always printed. '''
# class Transaction:
#     def process(self,amount):
#         try:
#             return int(amount)
#         except TypeError as e:
#             print(e)
#         except ValueError as e:
#             print(e)
#         finally:
#             print("process done successfully")
# t= Transaction()
# t.process("")

# '''• Create a class LoginSystem with a method login(password)
#     that raises an exception for an incorrect password and handles the exception outside the class.'''



    


