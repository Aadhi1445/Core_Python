# '''1. Bank Management System
# Create a Bank class with:
#  • balance variable
#  • deposit()
#  • withdraw()
#  • check_balance()
#  Create a User class that inherits Bank and displays the user's name.
#  Perform deposit, withdrawal, and balance check. '''
# class Bank:
#     def __init__(self,n,b):
#         self.balance=b
#         self.name=n
#     def deposit(self,amount):
#         if amount>0:
#             self.balance+=amount
#             print(f'{amount} successfully deposited\n'
#                   f'existing balance:{self.balance}')
#             return self.balance
#         else:
#             print("Invalid deposit amount")
#     def withdraw(self,amount):
#         if amount<=self.balance and amount>0:
#             self.balance-=amount
#             print(f'{amount} successfully withdrawn\n'
#                   f'existing balance:{self.balance}')
#             return self.balance
#         else:
#             print("Invalid withdrawn amount")
#     def check_balance(self):
#         print(f'{self.balance} is existing balance')
#         return self.balance
#     def display(self):
#         print(f'Name: {self.name}'
#               f'Balance: {self.balance}')
# class User(Bank):
#     def __init__(self,n,b=0):
#         super().__init__(n,b)
#     def display(self):
#         print(f"User's name: {self.name}")
# u1=User('Aadhya')
# u1.display()
# u1.check_balance()
# u1.deposit(5000)
# u1.deposit(0)
# u1.withdraw(250)
# u1.withdraw(0)
# print('-'*50)
# '''2. Employee Salary System
# Create an Employee class with:
# • emp_name
# • salary
# • display_details()
# Create a Manager class that inherits Employee and adds a bonus().
#  Display the total salary.'''
# class Employee:
#     def __init__(self,n,s):
#         self.name=n
#         self.salary=s
#     def display_details(self):
#         print(f'Name:{self.name}\n'
#               f'Salary:{self.salary}')
# class Manager(Employee):
#     def bonus(self,amount):
#         self.salary+=amount
# m1=Manager('Aadhya',50000)
# m1.display_details()
# m1.bonus(10000)
# print('Total_salary:',m1.salary)
# print('-'*50)
# '''Student Result System
# Create a Student class with:
# • Name
# • marks
# • display_marks()
# Create a Result class that inherits Student and
# calculates whether the student has passed or failed.'''
# class Student:
#     def __init__(self,n,m):
#         self.name=n
#         self.marks=m
#     def display_marks(self):
#         print(f'Name:{self.name}\nMarks:{self.marks}')
# class Result(Student):
#     def check(self):
#         if self.marks>=40:
#             print(f'{self.name} has Passed with Marks:{self.marks}')
#         else:
#             print(f'{self.name} has Failed with Marks:{self.marks}')
# s1=Result('Aadhya',56)
# s1.display_marks()
# s1.check()
# s2=Student('Parul',30)
# print('-'*50)
# '''4. Food Ordering System
# Using Multilevel Inheritance
# Class 1: Restaurant
#     • Create a method menu(item) that returns the price of the selected food item.
# Class 2: FoodCourt (inherits Restaurant) Create the following methods:
#     • display_menu() – Display the available food items.
#      • order() – Accept the food item from the user and allow multiple orders.
#      • billing() – Display the total bill and add a packing charge of ₹20.
# Class 3: Customer (inherits FoodCourt) • Create an object of the Customer class.
# • Call the order() method. '''
# class Restaurant:
#     def __init__(self,name,**kwargs):
#         self.menu=kwargs
#         self.name=name
# # r1=Restaurant('Shiva',Idly=20,dosa=50,bonda=30)
# class Food_court(Restaurant):
#     def display_menu(self):
#         print('------',Menu,'---------')
#         for key,value in self.menu.items():
#             print(f'{key}:{value}')
# f1=Food_court('Shiva',Idly=20,dosa=50,bonda=30)
# # f1.display_menu()
#     def order(self,*args):
#         l=list(args)
#         return l
# '''5. Movie Ticket Booking System Using Multilevel Inheritance
# Class 1: Movie
#     • Create a method ticket(movie) that returns the ticket price.
# Class 2: Booking (inherits Movie) Create the following methods:
#     • movies() – Display the available movies.
#     • selection() – Allow the user to book multiple tickets.
#     • billing() – Display the total amount and add a booking charge of ₹30.
# Class 3: Customer (inherits Booking)
#     • Create an object and call the selection() method.'''
# class Movie:
#     list={'Salaar':350,'Devara':250,'Darling':150,'Pushpa':80,'Fauzi':650,'Kalki':450}
#     def ticket(self,*movie):
#         for i in movie:
#             print(f'Price of {i} Movie : {self.list[i]}')
#             # return f'Price of {movie} Movie: {self.list[movie]}'
# class Booking(Movie):
#     def movies(self):
#         for k,v  in self.list.items():
#             print(k,':',v)
#     def selection(self,*args):
#         self.l=list(args)
#         print(*self.l,'movies are selected.')
#     def billing(self):
#         total_amount=0
#         for i in self.l:
#             total_amount+=self.list[i]
#         print(f'Total_amount included booking charge of ₹30: {total_amount+30}. ')
#         return f'Total_amount included booking charge of ₹30: {total_amount+30}. '
# class Customer(Booking):
#     pass
# c1=Customer()
# c1.movies()
# c1.ticket('Salaar','Devara','Fauzi')
# c1.selection('Salaar','Devara','Fauzi')
# c1.billing()
# print('-'*50)
# '''6. Online Course Enrollment System Using Multilevel Inheritance
# Class 1: Course
#     • Create a method fee(course) that returns the course fee.
# Class 2: Academy (inherits Course) Create the following methods:
#     • courses() – Display available courses.
#     • enroll() – Allow the user to enroll in multiple courses.
#     • billing() – Display the total fee and add a registration fee of ₹100.
# Class 3: Student (inherits Academy)
#     • Create an object and call the enroll() method'''
# class Course:
#     list={'Python':37000,'Java':35000,'DA':56000,'Cloud_Computing':25000}
#     def fee(self,course):
#         print(f'Fee of {course} is Rs.{self.list[course]}/-')
# class Academy(Course):
#     def courses(self):
#         print('Available Courses are:')
#         for i in self.list.keys():
#             print(' '*22,i)
#     def enroll(self,*args):
#         print('Enrolled in:')
#         for i in args:
#             print(' '*12,i)
#     def billing(self,*args):
#         total_fee=0
#         for i in args:
#             total_fee+=self.list[i]
#         print(f'Total_fee included with Rs.100/- Registration fee: {total_fee+100}/-')
# class Student(Academy):
#     pass
# a=Student()
# a.courses()
# a.enroll('Java','Python')
# a.billing('Java','Python','DA')
# print('-'*50)
# '''7. Cab Booking System Using Hierarchical Inheritance
# Class 1: Cab
#     • Create methods to calculate the fare for Bike, Auto, and Car rides.
# Class 2: Uber (inherits Cab)
#     • Create the methods menu(), booking(), and billing().
#     • Add 10% GST and apply a 15% discount if the bill is above ₹1000.
# Class 3: Ola (inherits Cab)
#     • Create the methods menu(), booking(), and billing().
#     • Add 12% GST and apply a 20% discount if the bill is above ₹1500.
# Driver Code
#     • Ask the user to choose Uber or Ola and call the booking() method.'''
# class Cab:
#     @staticmethod
#     def calculate():
#         pass
# class Ola(Cab):
#     price={'Car':15,'Bike':8,'Auto':10}
#     def menu(self):
#         for i,j in  self.price.items():
#             print(i,':',j)
#     def booking(self,k,m):
#         self.k=k
#         self.m=m
#         print(f'{k} is booked')
#     def billing(self):
#         total_bill=self.price[self.k]*self.m
#         total_bill=total_bill+((12/100)*total_bill)
#         if total_bill>1000:
#             total_bill=total_bill-((20/100)*total_bill)
#             return total_bill
#         else:
#             return total_bill
# class Uber:
#     price = {'Car': 16, 'Bike': 6, 'Auto': 12}
#     def menu(self):
#         for i,j in  self.price.items():
#             print(i,':',j)
#     def booking(self,k,m):
#         self.k=k
#         self.m=m
#         print(f'{k} is Booked')
#     def billing(self):
#         total_bill=self.price[self.k]*self.m
#         total_bill = total_bill + ((10 / 100) * total_bill)
#         if total_bill > 1000:
#             total_bill = total_bill - ((15 / 100) * total_bill)
#             return total_bill
#         else:
#             return total_bill
# def User():
#     app=input('Choose Uber or Ola')
#     vehicle=input('Bike','Car','Auto')
#     if app=='Uber':
#         u=Uber()
#     else:
#         u=Ola()
# '''10. ATM System Using Multiple Inheritance
# Class 1: SBI
#     • Create the methods deposit(amount) and check_balance().
# Class 2: UnionBank
#     • Create the methods withdraw(amount) and mini_statement().
# Class 3: ATM (inherits SBI and UnionBank)
#     • Create the methods menu() and transaction().
#     • Allow the user to perform banking operations.
# Driver Code • Create an object of the ATM class.
#   • Call the transaction() method.'''
# class SBI:
#     bank_balance=0
#     def deposit(self,amount):
#         self.bank_balance+=amount
#         print(f'{amount} amount is deposited.')
#     def check_balance(self):
#         print(f'Existing Bank Balance :{self.bank_balance}.')
# class UnionBank:
#     bank_balance=0
#     def withdrawn(self, amount):
#         if amount<=self.bank_balance:
#             self.bank_balance -= amount
#             print(f'{amount} amount is deposited.')
#         else:
#             print('Insufficient Funds')
#     def check_balance(self):
#         print(f'Existing Bank Balance :{self.bank_balance}.')
# class ATM(SBI,UnionBank):
#     def menu(self):
#         print(f'1:deposit\n'
#               f'2:withdraw\n'
#               f'3:check_balance')
#     def transaction(self):
#         k=int(input('Enter Ur Choice:'))
#         if k==1:
#             amount=int(input('Enter amount:'))
#             self.deposit(amount)
#         elif k==2:
#             amount = int(input('Enter amount:'))
#             self.withdrawn(amount)
#         elif k==3:
#             self.check_balance()
#         else:
#             print("Invalid Input")
# def driver_code(obj):
#     obj.transaction()
# driver_code(ATM())
# '''11. Paytm Application Using Multiple Inheritance
# Write a Python program to implement a Paytm Application using multiple inheritance.
# Class 1: MobileRecharge
#     • Create the methods recharge_plans() and mobile_recharge().
# Class 2: BusTicketBooking
#     • Create the methods display_buses() and book_ticket().
# Class 3: ElectricityBills
#     • Create the methods bill_details() and pay_bill().
# Class 4: Paytm (inherits MobileRecharge, BusTicketBooking, and ElectricityBills)
#     Create the following methods:
#         • menu() – Display the available services.
#         • services() – Allow the user to choose and use any service
#             (Mobile Recharge, Bus Ticket Booking, or Electricity Bill Payment).'''
# class Mobile_Recharge:
#     def recharge_plans(self):
#         print(f'199:[28 days Validity, 2GB data]\n'
#               f'249:[28 days Validity,2GB/Day]\n'
#               f'899:[90 days Validity,2GB/Day')
#     def mobile_recharge(self,amount):
#         print(f'{amount}-plan Recharge Successful')
# class Bus_Ticket_Booking:
#     def display_buses(self):
#         print("Satwik Travels\nSiva Travels\nPaaru Travels")
#     def book_ticket(self,bus):
#         print(f'Ticket is booked successfully for "{bus} " Travels ')
# class Electricity_bills:
#     def bill_details(self):
#         print('bill details')
#     def pay_bill(self):
#         print('Bill is successfully paid')
# class Paytm(Mobile_Recharge,Bus_Ticket_Booking,Electricity_bills):
#     def display(self):
#         print('------','Services','----------')
#         print('1:Mobile_Recharge\n2:Bus_Ticket_booking\n3:Electricity_Bill')
#     def services(self):
#         self.display()
#         k=int(input('Enter Ur Choice:'))
#         if k==1:
#             self.recharge_plans()
#             m=int(input('Enter Type Of Plan:'))
#             self.mobile_recharge(m)
#         elif k==2:
#             self.display_buses()
#             bus=input('Enter Type of Travels:')
#             self.book_ticket(bus)
#         elif k==3:
#             self.pay_bill()
#         else:
#             print("Invalid Input")
# p1=Paytm()
# p1.display()
# p1.services()



