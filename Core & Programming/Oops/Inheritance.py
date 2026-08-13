'''Inheritance'''
# class Animal:
#     def __init__(self,n):
#         self.name=n
#     def Eat(self):
#         print("Parent Class is called")
#         print(f"{self.name} is Eating")
# class Dog(Animal):
#     def bark(self):
#         print("Child class is called")
#         print(f"{self.name} is Barking")
# # d1=Dog()
# d1=Dog('German Shepherd')
# d1.bark()
# d1.Eat()
# a1=Animal('Golden Sparrow')
# # a1.bark()
# a1.Eat()

# class Vehicle:
#     def __init__(self,b,s):
#         self.brand=b
#         self.speed=s
#     def display_vehicle(self):
#         print(f'Brand={self.brand}\nSpeed={self.speed}')
# class Car(Vehicle):
#     def __init__(self,b,s,m):
#         super().__init__(b,s)
#         self.model=m
#     def display_car(self):
#         print(f'Model={self.model}')
# c1=Car('Hundai','80km/hr','Creta')
# c1.display_vehicle()
# c1.display_car()

# class Person:
#     def __init__(self,n,a):
#         self.name=n
#         self.age=a
# class Student(Person):
#     def __init__(self,n,a,m):
#         self.marks=m
#         super().__init__(n,a)
# s1=Student('Aadhya',22,50)
# print('Name:',s1.name,'\nAge:',s1.age,'\nMarks:',s1.marks)

# class Employee:
#     def __init__(self,n,s):
#         self.name=n
#         self.salary=s
# class Developer(Employee):
#     def __init__(self,n,s,l):
#         super().__init__(n,s)
#         self.language=l
#     def display(self):
#         print(f'Name:{self.name}\nSalary:{self.salary}\nLanguage:{self.language}')
# d1=Developer('Adhya',50000,'Python')
# d1.display()

# class Person:
#     def __init__(self,n,a):
#         self.name=n
#         self.age=a
# class Teacher(Person):
#     def __init__(self,n,a,s,sa):
#         super().__init__(n,a)
#         self.subject=s
#         self.salary=sa
#     def display(self):
#         print(f'Name:{self.name}\nAge:{self.age}\nSubject:{self.subject}\nSalary:{self.salary}')
# t1=Teacher('Parul',54,'Social',49000)
# t1.display()
'''Multilevel Inheritance'''
# class Animal:
#     def eat(self):
#         print("Animal is Eating")
# class Mammal(Animal):
#     def walk(self):
#         print("Mammal is walking")
# class Dog(Mammal):
#     def bark(self):
#         print("Dog is Barking!")
# d1=Dog()
# d1.bark()
# d1.walk()
# d1.eat()
'''Multiple Inheritance'''
# class Father:
#     def Father_property(self):
#         print("Child Inherited Father's Property")
# class Mother:
#     def Mother_property(self):
#         print("Child Inherited Mother Property")
# class Child(Father,Mother):
#     def Child_property(self):
#         self.Mother_property()
#         self.Father_property()
# c1=Child()
# c1.Child_property()
print('-'*50)
'''5. Hybrid Inheritance

Combination of two or more types of inheritance.

For example:

             Person
            /      \
       Employee   Student
            \      /
             Intern

Here you have:

Hierarchical inheritance: Person → Employee and Person → Student
Multiple inheritance: Employee + Student → Intern

Together, this forms hybrid inheritance.

This is similar to the example you were practicing earlier.'''
# class Person:
#     def __init__(self,n):
#         self.name=n
#     def person(self):
#         print("Person class")
# class Employee(Person):
#     def __init__(self,s,n):
#         super().__init__(n)
#         self.salary = s
#     def employee(self):
#         print("Employee is inherited from Person class")
# class Student(Person):
#     def __init__(self,c,n):
#         super().__init__(n)
#         self.college = c
#     def student(self):
#         print('student is inherited from Person class')
# class Intern(Employee,Student):
#     def __init__(self,d,s,c,n):
#         self.duration=d
#         super().__init__(s,n)
#         super().__init__(c,n)
#     def Intern(self):
#         print(f'Name:{self.name}\nCollege:{self.college}\nSalary:{self.salary}\nDuration:{self.duration}')
#     def display(self):
#         self.Intern()
#         self.employee()
#         self.person()
#         self.Intern()
e1=Employee(15000,'VSM College of Engineering','Aadhya ')
# i1.display()
