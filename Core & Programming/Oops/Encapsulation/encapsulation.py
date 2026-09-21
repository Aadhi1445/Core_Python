# '''1.  Create a BankAccount class that stores:
#     • account number
#     • balance (should not be directly modifiable)
# You must: 1. Make the balance attribute inaccessible from outside.
#         2. Provide functions to deposit/withdraw that validate the amount.
#         3. Prevent withdrawal if balance becomes negative.
#         4. Show what happens if someone tries to modify balance directly
#             and why encapsulation prevents it.'''
# class BankAccount:
#     def __init__(self,Acc_no):
#         self.Acc_no=Acc_no
#         self.__balance=0
#     def get_balance(self):
#         return self.__balance
#     def deposit(self,amount):
#         if amount>0:
#             self.__balance+=amount
#             print(f'"{amount}/-" Amount is successfully deposited.')
#         else:
#             print('Invalid  Deposit Amount..!')
#     def withdrawal(self,amount):
#         if amount<1:
#             print('Amount should be positive..!')
#         elif amount>self.__balance:
#             print('Insufficient Funds..!')
#         elif self.__balance<0:
#             print('Withdrawnal is Prevented..!')
#         else:
#             self.__balance-=amount
#             print(f'{amount}/-Withdrawn Successfully.')
# b1=BankAccount('1422062883')
# # b1.deposit(5000)
# b1.deposit(0)
# # print(b1.balance)  -- it throws attribute  error
# print(b1.get_balance())
# b1.withdrawal(2000)
# b1.deposit(5000)
# b1.withdrawal(2000)
# print(b1.get_balance())
# b1.withdrawal(3001)
# b1.withdrawal(-1)
# '''2. Design a Student class where marks:
#     • should always be between 0 and 100
#     • should never be set directly Enable updating marks only through
#         a controlled method that performs range checks.
# Demonstrate:
#     • trying to assign marks manually
#     • why encapsulation protects invalid states '''
# class Student:
#     def __init__(self,marks):
#         if 0<=marks<=100:
#             self.__marks=marks
#         else:
#             print('Marks should be in between 0 to 100')
#     @property
#     def marks(self):
#         return self.__marks
#     @marks.setter
#     def marks(self,marks):
#         if 0<=marks<=100:
#             self.__marks=marks
#         else:
#             print('Marks should be in between 0 to 100')
# s1=Student(50)
# # s1=Student(101)
# # s1.marks=100
# # print(s1.marks)# it throws error
# # print(s1.__dict__)# this method shows the attributes /data stored in an object in dictionary format
# print(s1.marks)
# print(s1.marks)
# s1.marks=90
# print(s1.marks)
# s1.marks=901
# print(s1.marks)
# # print(s1.__marks)#it throws error
# print(s1._Student__marks,'marks')# it is not a good practice of accesing this like as a developer .
# '''3. Create a SecureFile class that:
#     • stores content privately
#     • provides a method read(password)
#     • refuses access if the password is incorrect
#     • logs an "Unauthorized attempt" internally (cannot be accessed from outside) '''
# class Securefile:
#     def __init__(self,content,password):
#         self.__content=content
#         self.__password=password
#         self.__logs=[]
#     def read(self,password):
#         if password==self.__password:
#             return self.__content
#         else:
#             self.__logs.append('Unauthorised Attempt')
#             return 'Refused Access'
# s1=Securefile('img','Aditya@1445')
# print(s1.read('Aditya@1445'))
# print(s1.read('Aditya@1495'))
# '''4.Design an Employee class where:
#     • salary is hidden
#     • outsiders cannot read salary directly
#     • use getter method that logs each access attempt
#     • provide a method to update salary but only if the new salary is higher
#         (prevent accidental downgrade)'''
# class Employee:
#     def __init__(self,salary):
#         self.__salary=salary
#         self.__logs=[]
#     @property
#     def salary(self):
#         self.__logs.append('Salary Accessed')
#         return self.__salary
#     @salary.setter
#     def salary(self,new_salary):
#         if new_salary>self.__salary:
#             self.__salary=new_salary
# e1=Employee(50000)
# # e1.salary()# here salary is an property so we should not call it. due to it acts like an attribute .
# print(e1.salary)
# '''5. Create a Product class where:
#     • price cannot be negative
#     • discount cannot exceed 70%
#     • internal final price calculation should not be directly exposed
#         Provide only one public method get_final_price(). '''
# class Product:
#     def __init__(self,price):
#         if price>=0:
#             self.__price=price
#         else:
#             raise ValueError('Price cannot be Negative')
#     def get_final_price(self,dis):
#         if dis>70:
#             return 'Discount cannot be exceeds 70%'
#         else:
#             return (self.__price-((dis/100)*self.__price))
# p1=Product(100)
# # p1=Product(-100)
# # print(p1.get_final_price(71))
# print(p1.get_final_price(50))
# '''6. Create a Character class with:
#     • private _health
#     • methods to damage(points) and heal(points)
#     • health cannot drop below 0 or exceed max limit
#     • expose only current health through a read-only getter'''
# class Character:
#     def __init__(self,name):
#         self.__health=100
#         self.name=name
#     def get_health(self):
#         return self.__health
#     def damage(self,other,points):
#         if points>0 and points <=100:
#             if points<other.__health:
#                 other.__health-=points
#             else:
#                 other.__health=0
#         else:
#             print('Damage Points Should be in range of 0-100')
#     def heal(self,points):
#         if points>0 and points <=100:
#             if points+self.__health>100:
#                 self.__health=100
#             else:
#                 self.__health+=points
#         else:
#             print("Heal Points Should be in range of 0-100")
# c1=Character('Aadhi')
# c2=Character('Siva')
# print(c1.get_health())
# c2.damage(c1,150)
# print(c1.get_health())
# c1.heal(500)
# print(c1.get_health())
# '''7. Create:
#     • An Engine class with private state like temperature
#     • A Car class that uses an Engine but should:
#                 o Not allow users to manipulate engine temperature
#                 o Only expose methods like start_car() or cool_engine()
#     Demonstrate why giving direct engine access is dangerous.'''
# class Engine:
#     def __init__(self,type):
#         self.type=type
#         self.__temp=38
#     def get_temp(self):
#         return self.__temp
#     def start_engine(self):
#         self.__temp-=10
#         print('Car is Started')
#     def stop_engine(self):
#         self.__temp=38
#         print('car is Stopped')
# class Car:
#     def __init__(self,brand,engine):
#         self.brand=brand
#         self.engine=engine
#     def start_car(self):
#         self.engine.start_engine()
#     def stop_car(self):
#         self.engine.stop_engine()
# c1=Car('Fortuner',Engine('inline_v'))
# c1.start_car()
# '''8. Create a ShoppingCart class where:
#     • items are stored privately
#     • users cannot directly modify item list
#     • only add/remove methods are allowed
#     • provide a method to get a safe copy of the cart items
#             (not direct reference to internal list)'''
# class Shoppingcart:
#     def __init__(self,*args):
#         self.__list=list(args)
#     def get_list(self):
#         return self.__list.copy()
#     def add_item(self,other):
#         return self.__list.append(other)
#     def remove_item(self, other):
#         return self.__list.remove(other)
#     def __add__(self, other):
#         # print(2)
#         return Shoppingcart(self.__list+other)
# c1=Shoppingcart('Apple','Banana','Guava','Orange')
# print(c1.get_list())
# c1.add_item('Grapes')
# # print(c1.get_list())
# c1+'fghj'
# print(c1.get_list())
#
#
#


'''9. Implement a class incorrectly first: 
    • Attendance stored in a list 
    • Exposed directly so any outside code can modify it Then redesign properly: 
    • Make attendance private 
    • Provide controlled methods for marking attendance only Explain the difference. '''

'''10. Create a class using @property and @setter for a private attribute. 
    Then: 1. Show correct usage 
          2. Show how forgetting to use underscore prefix breaks encapsulation 
          3. Show what happens if you implement a setter without validation Focus: 
                            Python-specific encapsulation pitfalls, misuse of properties.'''
