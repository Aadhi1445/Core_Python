'''Question 1:
Bank Account Operations
Create a class BankAccount with:
•	attributes: account_holder, balance
•	instance method: deposit(amount)
•	instance method: withdraw(amount)
Implement these magic methods:
•	__str__() → display account details
•	__add__() → add balances of two accounts
•	__sub__() → subtract balances
•	__eq__() → compare if two accounts have same balance
•	__lt__() → check which account has lower balance
•	__getattribute__() → print a message whenever an attribute is accessed
•	__setattr__() → prevent setting negative balance
Demonstrate creating two accounts and using all operations.'''

# class Bank_acc:
#     def __init__(self,name,Acc_num,balance=0):
#         self.name=name
#         self.Acc_num=Acc_num
#         self.balance=balance
#     def deposit(self,x):
#         self.balance=self.balance+x
#         return self.balance
#     def withdraw(self,y):
#         if y >self.balance:
#             print('Insufficient Funds')
#         else:
#             self.balance-=y
#             print(self.balance)
#     def __str__(self):
#         return f'Acc_holder:{self.name}\nAcc_Num:{self.Acc_num}\nbalance:{self.balance}\n'
#     def __add__(self, other):
#         return self.balance+other.balance
#     def __sub__(self, other):
#         if self.balance>other.balance:
#             return self.balance-other.balance
#         else:
#             return other.balance-self.balance
#     def __eq__(self, other):
#         return self.balance==other.balance
#     def __lt__(self, other):
#         if self.balance<other.balance:
#             return f'{c1.name} has less balance'
#         else:
#             return f'{other.name} has less balance'
# c1=Bank_acc('parul',43534543,5000)
# c2=Bank_acc('Adhya',987654,3000)
# print(c1)
# print(c2)
# print(c1.deposit(2000))
# print(c2.deposit(3000))
# c1.withdraw(2000)
# c2.withdraw(10000)
# print(c1)
# print(c2)
# print('total balance:',c1+c2)
# print('difference:',c1-c2)
# print()
# print(c1==c2)
# print(c1<c2)

'''Question 2:
 Product Price Comparison
Create a class Product with:
•	attributes: name, price, quantity 
•	method: total_price() 
Implement:
•	__str__() 
•	__add__() → add total prices of two products 
•	__mul__() → multiply product price by a number 
•	__gt__() → compare which product has greater total value 
•	__eq__() → compare prices 
•	__getattr__() → return "Attribute not found" for missing attributes 
# •	__setattr__() → do not allow price less than 0 '''
# class Product:
#     def __init__(self,name,price,quantity):
#         self.name=name
#         self.price=price
#         self.quantity=quantity
#         # self.total_price=price*quantity
#     def total_price(self):
#         return self.price*self.quantity
#     def __add__(self, other):
#         return self.price+other.price
#     def __mul__(self, other):
#         return self.price*other.price
#     def __str__(self):
#         return (f'Product name:{self.name}\nProduct price:{self.price}\nQuantity:{self.quantity}\ntotal_price:{self.total_price}\n')
#     def __gt__(self, other):
#         if self.total_price()>other.total_price():
#             return f'{self.name} has greater price'
#         else:
#             return f'{other.name} has greater price'
#     def __eq__(self, other):
#         return self.price==other.price
# p1= Product('Aadhya',200,2)
# p2=Product('Parul',150,3)
# # print(p1)
# # print(p2)
# # print(p1>p2)
# # print(p1*p2)
# # print(p1==p2)
# print(p1.total_price())
# print(p2.total_price())
# print(p1>p2)

'''________________________________________
Question 3: Student Marks
Create a class Student with:
•	attributes: name, marks 
•	method: grade() 
Implement:
•	__str__() 
•	__add__() → add marks of two students 
•	__truediv__() → divide marks by a number 
•	__ge__() → check if one student scored greater than or equal to another 
•	__lt__() → check if one student scored less 
•	__getattribute__() → track attribute access 
# •	__setattr__() → marks must be between 0 and 100 '''
# class Student:
#     def __init__(self,name,marks):
#         self.name=name
#         self.marks=marks
#
#     def grade(self):
#         if self.marks>90:
#             return f'{self.name} scored "A+" grade'
#         elif self.marks>80:
#             return f'{self.name} scored "A" grade'
#         elif self.marks>70:
#             return f'{self.name} scored "B" grade'
#         elif self.marks>60:
#             return f'{self.name} scored "C" grade'
#         elif self.marks>50:
#             return f'{self.name} scored "D" grade'
#         elif self.marks>40:
#             return f'{self.name} scored "E" grade'
#         else:
#             return f'{self.name} scored "F" grade'
#     def __str__(self):
#         return f'Student_Name:{self.name}\nMarks:{self.marks}\n{self.grade()}\n'
#     def __add__(self, other):
#         return self.marks+other.marks
#     def __truediv__(self, other):
#         return  self.marks/other.marks
#     def __ge__(self, other):
#         if self.marks>other.marks:
#             return f'{self.name} has scored Great Marks than {other.name}'
#         elif self.marks==other.marks:
#             return f'{self.name} has scored Equal  Marks  {other.name}'
#     def __lt__(self, other):
#         if self.marks<other.marks:
#             return f'{self.name} has scored Less Marks than {other.name}'
#         else:
#             return f'{other.name} has scored Less Marks than {self.name}'
# s1=Student('Aadhya',78)
# print(s1)
# s2=Student('paaru',59)
# s3=Student('shiva',59)
# print(s2)
# print(s1+s2)
# print(s1/s2)
# print(s1>s2)
# print(s1<s2)
# print(s1>=s2)
# print(s2>=s3)
'''________________________________________
Question 4: Rectangle Area Comparison
Create a class Rectangle with:
•	attributes: length, breadth 
•	method: area() 
Implement:
•	__str__() 
•	__add__() → add areas of two rectangles 
•	__sub__() → subtract areas 
•	__eq__() → compare areas 
•	__gt__() → check which rectangle has larger area 
•	__getattr__() → handle missing attributes 
•	__setattr__() → length and breadth must be positive'''
# class Rectangle:
#     def __init__(self,n,l,b):
#         self.length=l
#         self.breadth=b
#         self.name=n
#         self.area=l*b
#     def area(self):
#         return self.area
#     def __add__(self, other):
#         return f'Additon of two areas :{self.area+other.area}'
#     def __sub__(self, other):
#         if self.area>other.area:
#             return f'substraction of two areas: {self.area-other.area}'
#         else:
#             return f'substraction of two areas:{other.area-self.area}'
#     def __eq__(self, other):
#         if self.area==other.area:
#             return f'{self.name}&{other.name} has equal area'
#         else:
#             return f'{self.name}&{other.name} has  No equal area'
#     def __gt__(self, other):
#         if self.area>other.area:
#             return f'{self.name} has Greater Area'
#         else:
#             return f'{other.name} has Greater Area'
# r1=Rectangle('r1',20,10)
# r2=Rectangle('r2',10,5)
# print(r1+r2)
# print(r1-r2)
# print(r1>r2)
'''________________________________________
Question 5: Employee Salary System
Create a class Employee with:
•	attributes: name, salary 
•	method: annual_salary() 
Implement:
•	__str__() 
•	__add__() → add salaries of two employees 
•	__mul__() → calculate salary after multiplying by months 
•	__ne__() → check if salaries are not equal 
•	__le__() → check if one salary is less than or equal to another 
•	__getattribute__() → log every attribute access 
•	__setattr__() → salary cannot be below 10000 '''
# class Employee:
#     def __init__(self,name,salary):
#         self.name=name
#         self.salary=salary
#     def annual_salary(self):
#         return self.salary*12
#     def __str__(self):
#         return f'name:{self.name}\nsalary:{self.salary}\n'
#     def __add__(self, other):
#         return Employee("total",self.salary+other.salary)
#         # return f'addition of both salaries:{self.salary+other.salary}'
#     def __mul__(self, other):
#         return f'Multiplication of  both salary :{self.salary*other.salary}'
#     def __ne__(self, other):
#         if self.salary!=other.salary:
#             return f'{self.name} & {other.name} Salaries are not Equal'
#         else:
#             return f'{self.name} & {other.name} Salaries are Equal'
#
#     def __le__(self, other):
#         if self.salary<other.salary:
#             return f'{self.name} has Less salary than {other.name}'
#         elif self.salary==other.salary:
#             return f'{self.name} & {other.name} have equal salaries'
#         else:
#             return f'{self.name} & {other.name}  salaries are not <= to each other'
#
# e1=Employee('Aadhya',5000)
# e2=Employee('paaru',4000)
# e3=Employee('shiva',5000)
# # print(e1<=e2)
# # print(e1!=e2)
# # print(e1==e3)
# # print(e1*e3)
# print(e1+e2+e3)
'''________________________________________
Question 6: Book Object Comparison
Create a class Book with:
•	attributes: title, author, pages 
•	method: reading_time()
Assume 1 page takes 2 minutes. 
Implement:
•	__str__() 
•	__add__() → add pages of two books 
•	__floordiv__() → divide pages by number of days 
•	__gt__() → compare books based on pages 
•	__eq__() → compare books based on title 
•	__getattr__() → return custom message for missing attribute 
•	__setattr__() → title cannot be empty and pages must be positive 
________________________________________
Question 7: Shopping Cart
Create a class CartItem with:
•	attributes: item_name, price, quantity 
•	method: final_amount() 
Implement:
•	__str__() 
•	__add__() → add final amounts of two cart items 
•	__mod__() → find remainder after applying a discount value 
•	__lt__() → compare item total amount 
•	__ge__() → compare quantity 
•	__getattribute__() → display which attribute is being accessed 
•	__setattr__() → quantity cannot be less than 1 
________________________________________


Question 8: Time Duration
Create a class TimeDuration with:
•	attributes: hours, minutes 
•	method: total_minutes() 
Implement:
•	__str__() 
•	__add__() → add two time durations 
•	__sub__() → subtract two time durations 
•	__eq__() → compare total minutes 
•	__gt__() → check longer duration 
•	__getattr__() → handle invalid attribute access 
•	__setattr__() → minutes must be between 0 and 59 
________________________________________


Question 9: Laptop Specification
Create a class Laptop with:
•	attributes: brand, ram, price 
•	method: upgrade_ram(extra_ram) 
Implement:
•	__str__() 
•	__add__() → add prices of two laptops 
•	__mul__() → multiply price for bulk purchase 
•	__lt__() → compare price 
•	__eq__() → compare RAM 
•	__getattribute__() → print access message 
•	__setattr__() → RAM and price must be positive 
________________________________________'''
'''Question 10: Game Player
Create a class Player with:
•	attributes: name, health, attack_power 
•	method: attack(enemy) 
Implement:
•	__str__() 
•	__add__() → combine attack powers 
•	__sub__() → reduce health after attack 
•	__gt__() → compare health 
•	__eq__() → compare attack power 
•	__getattr__() → return custom message for unavailable player stat 
•	__setattr__() → health cannot go below 0 '''
# class Player:
#     def __init__(self,name,health,attack_power):
#         self.name=name
#         self.health=health
#         self.attack_power=attack_power
#     def __str__(self):
#         return f' Player_name:{self.name}\nPlayer_health:{self.health}\nPlayer_attack_power:{self.attack_power}\n'
#     def attack(self,enemy):
#         enemy.health=enemy.health-self.attack_power
#         return enemy.health
#     def __add__(self, other):
#         return f'comibnation of both attack_powers {self.attack_power+other.attack_power}'
#     def __sub__(self, other):
#         other.health=self.attack(other)
#         return f'the health of enemy after attack is  {other.health}'
#     def __gt__(self, other):
#         if self.health>other.health:
#             return f'{self.name} has more health'
#         else:
#             return f'{other.name} has more health'
#     def __eq__(self, other):
#         return self.attack_power==other.attack_power
# p1=Player('Aadhya',100,25)
# p2=Player('Parul',100,30)
# print(p2)
# print(p1-p2)
# print(p1+p2)
# print(p1==p2)
# print(p1>p2)
# print(p2)




'''class Shopping:
    def __init__(self):
        self.cart=[]
    def __str__(self):
        return f'{ self}'
c1=Shopping()
print(c1)
  [Previous line repeated 746 more times]
RecursionError: maximum recursion depth exceeded  
------>what happened in this '''

# class Shopping:
#     def __init__(self):
#         self.cart=[]
#     def __add__(self, other):
#         self.cart.append(other)
#         return self
# c1=Shopping()
# c1+'Aadhya'+'paaru'
# print(c1.cart)
# # print(type(c1.cart))
# # print(type(Shopping))
# # print(type(c1))

# class Shopping:
#     def __init__(self):
#         self.cart=[]
#     def __add__(self, other):
#         k=self.cart.append(other)
#         return k
# c1=Shopping()
# # c2=Shopping()
# c1+'Aadhya'+'Parul'
# # c2+'Dinosaur'+'Cheetah'
# print(c1.cart)

class Employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
    def annual_salary(self):
        return self.salary*12
    def __str__(self):
        return f'name:{self.name}\nsalary:{self.salary}\n'
    def __add__(self, other):
        return Employee("t",self.salary+other.salary)
        # return f'addition of both salaries:{self.salary+other.salary}'
    def __mul__(self, other):
        return f'Multiplication of  both salary :{self.salary*other.salary}'
    def __ne__(self, other):
        if self.salary!=other.salary:
            return f'{self.name} & {other.name} Salaries are not Equal'
        else:
            return f'{self.name} & {other.name} Salaries are Equal'

    def __le__(self, other):
        if self.salary<other.salary:
            return f'{self.name} has Less salary than {other.name}'
        elif self.salary==other.salary:
            return f'{self.name} & {other.name} have equal salaries'
        else:
            return f'{self.name} & {other.name}  salaries are not <= to each other'

e1=Employee('Aadhya',5000)
e2=Employee('paaru',4000)
e3=Employee('shiva',5000)
e4=Employee('shiva',5000)
e5=Employee('shiva',5000)

# print(e1<=e2)
# print(e1!=e2)
# print(e1==e3)
# print(e1*e3)
print(e1+e2+e3+e4+e5)
