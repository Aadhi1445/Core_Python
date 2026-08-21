'''• Create a base class Animal with a method sound().
 Create a derived class Dog that overrides the sound() method.
 Demonstrate method overriding.'''
# class Animal:
#     def sound(self):
#         print("Animal sound Method")
# class Dog(Animal):
#     def sound(self):
#         print("Animal Sound Method is overrides")
# a1=Animal()
# a1.sound()
# d1=Dog()
# d1.sound()
'''• Create class A with method show().
 Create class B(A) that overrides show() and
  also calls the parent method using super().'''
# class A:
#     def show(self):
#         print("show method of A class")
# class B(A):
#     def show(self):
#         print("Show of A class is overrides")
#         super().show()
# b1=B()
# b1.show()
'''• Create multi-level inheritance with classes A → B → C,
 each having a method display() printing the class name.
 Create object of C and call display(), showing method resolution.'''
# class A:
#     def display(self):
#         print("A class")
# class B(A):
#     def display(self):
#         print("B class")
#         super().display()
# class C(B):
#     def display(self):
#         print('C class')
#         super().display()
# c1=C()
# print(C.mro())
# c1.display()
'''• Implement hierarchical inheritance using a base class Vehicle and
 two child classes Car and Bike, each defining a method wheels().'''
# class Vehicle:
#     def wheels_info(self):
#         print("A vehicle consists of minimum")
# class Car(Vehicle):
#     def wheels(self):
#         print('Car has 4 wheels')
# class Bike(Vehicle):
#     def wheels(self):
#         print('Bike has 2  wheels')
# c1=Car()
# c1.wheels()
# c1.wheels_info()
# b1=Bike()
# b1.wheels_info()
# b1.wheels()
'''• Create class Employee with an instance method salary(). 
Create class Manager(Employee) that overrides salary() and adds an incentive.
 Demonstrate both outputs.'''
# class Employee:
#     def salary(self):
#         print("Instance salary method")
# class Manager(Employee):
#     def salary(self):
#         print('Adds an incentive to employees salary')
# e=Employee()
# e.salary()
# m=Manager()
# m.salary()
'''• Create class University with a class variable and a class method.
 Inherit it into class College and access the parent’s class variable from the child class. '''
class University:
    name='JNTUK'
    @classmethod
    def university(cls):
        print(f'Name:{cls.name}')
class College(University):
    def college(self):
        print(f'College Name:{self.name}')
        print(f'College Name:{University.name}')
        print(f'College Name:{College.name}')
        print(f'College Name:{College.name}')
c1=College()
print(c1.name)
c1.college()

'''• Create class MathOps with a static method add(a, b).
 Create class AdvancedOps(MathOps) and use the static method without overriding it.'''
# class MathOps:
#     @staticmethod
#     def add(a,b):
#         print('static method',a+b)
# class AdvancedOps(MathOps):
#     pass
# AdvancedOps.add(2,3)
# a=AdvancedOps()
# a.add(3,6)
''' • Create two classes Father and Mother, both defining a method skills().
 Create class Child(Father, Mother) and check which skills() runs using MRO.'''
# class Father:
#     def skills(self):
#         print('Father class')
# class Mother:
#     def skills(self):
#         print('Mother Class')
# class Child(Father,Mother):
#     pass
# print(Child.mro())
# c=Child()
# c.skills()
# class Child(Mother,Father):
#     pass
# c=Child()
# c.skills()

''' • Create an abstract class Shape with an abstract method area().
 Create class Rectangle(Shape) that implements the area() method.'''
# class :


'''• Create class Person with a constructor __init__(name).
 Create class Student(Person) with constructor __init__(name, roll). 
 Use super() to call the parent constructor.'''
# class Person:
#     def __init__(self,n):
#         print('Parent constructor called')
#         self.name=n
# class Student(Person):
#     def __init__(self,n,r):
#         super().__init__(n)
#         self.roll=r
# s1=Student('Aadhya',22)
