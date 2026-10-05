from abc import ABC,abstractmethod

from IPython.core.formatters import PDFFormatter

# '''1. Design a banking system with:
#     • An abstract base class Account
#         with deposit(),
#         withdraw(),
#         calculate_interest().
#     • Subclasses:
#         SavingsAccount,
#         CurrentAccount,
#         FixedDepositAccount.
#     • Each account must:
#         o Encapsulate balance (private)
#         o Provide controlled access through properties
#         o Override interest calculation differently
#     • Include a static method to validate amount.
#     • Include a class method to update bank-wide interest policies.
#     Demonstrate:
#         • Polymorphic behavior by iterating through all account types
#         • Preventing direct access to balance
#         • Multiple interest strategies'''
# class Account(ABC):
#     def __init__(self,acc_no,balance=0):
#         self.__balance=balance
#         self.acc_no=acc_no
#     @abstractmethod
#     def deposit(self,amount):
#         if amount>0:
#             self.__balance+=amount
#             print(f'{amount} successfully Deposited' )
#         else:
#             print('Invalid Amount')
#     @abstractmethod
#     def withdraw(self,amount):
#         if amount<= self.__balance:
#             self.__balance-=amount
#             print(f'{amount} successfully withdrawn')
#         else:
#             print('Insufficient fund    s')
#     @abstractmethod
#     def cal_interest(self):
#         pass
#     def get_balance(self):
#         return (f'Account : {self.acc_no}\n'
#                 f'Balance: {self.__balance}')
#     # @abstractmethod
#     @staticmethod
#     def validate_amount(amount):
#         if amount>0:
#             return 'Amount is Validated'
#         else:
#             return 'Invalid Amount'
# class Savings_acc(Account):
#     def deposit(self,amount):
#         super().deposit(amount)
#     def withdraw(self,amount):
#         super().withdraw(amount)
#     def cal_interest(self,amount):
#         print("hey")
#         interest= (0.03*amount)
#         print(f'{interest} for {amount} in Savings_Account\n'
#                 f'Interest Rate is : "3%"')
# class Current_Account(Account):
#     def deposit(self,amount):
#         super().deposit(amount)
#     def withdraw(self,amount):
#         super().withdraw(amount)
#     def cal_interest(amount):
#         interest= amount+(0.05*amount)
#         return (f'{interest} for {amount} in Current_Account\n'
#                 f'Interest Rate is : "5%"')
# class Fixed_Deposit(Account):
#     def deposit(self,amount):
#         super().deposit(amount)
#     def withdraw(self,amount):
#         super().withdraw(amount)
#     def cal_interest(amount):
#         # print(1)
#         interest= amount+(0.15*amount)
#         return (f'{interest} for {amount} in Fixed_Deposit_Account\n'
#                 f'Interest Rate is : "15%"')
# def acc(k,amount):
#     k.deposit(amount)
#     k.withdraw(amount)
#     k.cal_interest(amount)
# acc(Savings_acc(123456),200)

# fd=Fixed_Deposit('1444100638',5000)
# print(fd.get_balance())
# fd.deposit(3000)
# fd.cal_interest()






# '''2. Build:
#     • Vehicle base class
#     • Car, Bike, Auto subclasses
#     • A Driver class that contains a Vehicle
#     • A Ride class that:
#             o Calculates fare differently depending on the type of vehicle (polymorphism)
#             o Stores driver + vehicle combination
#             o Protects internal fare formula through encapsulation
#     Also:
#         • Use __str__ to print readable ride summaries.
#                 Show how composition + polymorphism interact.'''
# class Vehicle(ABC):
#     @abstractmethod
#     def fare(self):
#         pass
# class Car(Vehicle):
#     def fare(self,km):
#         return km*30
# class Auto(Vehicle):
#     def fare(self,km):
#         return km*20
# class Bike(Vehicle):
#     def fare(self,km):
#         return km*15
# class Driver:
#     def __init__(self,name,vehicle):
#         self.name=name
#         self.automobile=vehicle
# class Ride:
#     def cal_fare(self,obj,distance):
#         return obj.fare(distance)
# r1=Ride()
# print(r1.cal_fare(Bike(),50))
# ''' 3. Create:
#     • Abstract class PaymentMethod with   pay(),  validate()
#     • Subclasses: CardPayment, WalletPayment, UPIPayment
#     • Encapsulate user balance
#     • Use @property to control reading available funds
#     • Overload + operator to combine two payment methods into “split payment”
#     • Demonstrate polymorphism through a checkout loop.'''
# class PaymentMethod(ABC):
#     def __init__(self,bal):
#         self.__balance=bal
#     @abstractmethod
#     def pay(self):
#         pass
#     @abstractmethod
#     def validate(self):
#         pass
#     @property
#     def get_balance(self):
#         return self.__balance
#     def __add__(self, other):
#         return self.splitPayment(other)
#     def splitPayment(self,other):
#         amount1=int(input('Enter amount : '))
#         amount2=int(input('Enter amount : '))
#         if (amount1<=self.__balance) and (amount2<=other.__balance):
#             self.__balance-=amount1
#             other.__balance-=amount2
#             return 'Payment Done'
#         else:
#             return 'InSufficient Funds'
# class CardPayment(PaymentMethod):
#     def pay(self):
#         print('Payment done through "CardPayment"')
#     def validate(self):
#         print('Validation done through "CardPayment"')
# class WalletPayment(PaymentMethod):
#     def pay(self):
#         print('Payment done through "WalletPayment"')
#     def validate(self):
#         print('Validation done through "WalletPayment"')
# class UPIPayment(PaymentMethod):
#     def pay(self):
#         print('Payment done through "UPIPayment"')
#     def validate(self):
#         print('Validation done through "UPIPayment"')
# cp=CardPayment(5000)
# wp=WalletPayment(8000)
# upi=UPIPayment(10000)
# print(cp+wp)
# print(wp+upi)
# print(cp+upi)
# def payment(obj):
#     obj.pay()
#     obj.validate()
# payment(cp)
# '''4. Create classes:
#     • Person → base
#         • MedicalStaff(Person)
#         • Doctor(MedicalStaff)
#         • Surgeon(Doctor)
#     Requirements:
#         • Hide sensitive data (e.g., salary, patient notes)
#         • Abstract method perform_duty()
#         • Each level overrides the method with more specific behavior
#         • Use super() to chain constructor calls Demonstrate consistency across hierarchy.'''
# class Person(ABC):
#     def __init__(self,name):
#         self.__name=name
#     @abstractmethod
#     def person_duty(self):
#         print('Taking Medicine')
#     def get_name(self):
#         return self.__name
# class MedicalStaff(Person):
#     def __init__(self,name,department,notes,salary):
#         self.department=department
#         self.__patient_notes=notes
#         self.__salary=salary
#         super().__init__(name)
#     def get_salary(self):
#         return self.__salary
#     def get_patient_notes(self):
#         return self.__patient_notes
#     def person_duty(self):
#         print('Medical_Staff duties')
# class Doctor(MedicalStaff):
#     def __init__(self,name,department,specialization,notes,salary):
#         self.specialization=specialization
#         super().__init__(name,department,notes,salary)
#     def person_duty(self):
#         print('Doctor duties')
# class Surgeon(Doctor):
#     def __init__(self,name,department,specialization,surgery_type,notes,salary):
#         self.surgery_type=surgery_type
#         super().__init__(name,department,specialization,notes,salary)
#     def person_duty(self):
#         print('Surgeon duties')
# s1=Surgeon('Aditya','ICU','Heart','Left_Artery','Age:22,Village:Someswaram,Gender:Male',50000)
# print(s1.get_salary())

# '''5. Classes:
#         • User
#         • Instructor(User)
#         • Student(User)
#         • TeachingAssistant(Student, Instructor)
#       Requirements:
#         • Track course assignments privately
#         • Ensure TAs override submit_work() and grade_work()
#         • Print MRO and explain how Python resolves conflicts '''
# class User:
#     def __init__(self,name,email):
#         self.name = name
#         self.email=email
#         self.assignments=[]
#     def add_assignment(self,assignment):
#         return self.assignments.append(assignment)
# class Instructor(User):
#     def __init__(self,name,email):
#         super().__init__(name,email)
#     def grade_work(self):
#         print('Work is Issued')
# class Student(User):
#     def __init__(self,name,email):
#         super().__init__(name,email)
#     def submit_work(self):
#         print('Work is Submitted')
# class TeachingAssistant(Student,Instructor):
#     def submit_work(self):
#         super().submit_work()
#     def grade_work(self):
#         super().grade_work()
# # print(TeachingAssistant.mro())
# ta=TeachingAssistant('Aditya','Aditya965258@gmail.com')
# ta.add_assignment('Python')
# ta.add_assignment('Java')
# print(ta.assignments)

# '''6. Create:
#         • Product class with private price and quantity
#         • Warehouse class containing multiple products
#         • Overload:
#             o + to merge warehouses
#             o len() to return number of unique products
#             o in operator to check if product exists
#         • Provide class method to track total warehouses created '''
# class Product:
#     def __init__(self,name,price,quantity):
#         self.__price = price
#         self.name=name
#         self.__quantity = quantity
#     def get_price(self):
#         return self.__price
#     def get_quantity(self):
#         return self.__quantity
#     def __str__(self):
#         return (f'Name: {self.name}\n'
#                 f'Price: {self.get_price()}\n'
#                 f'Quantity: {self.get_quantity()}')
# class Warehouse:
#     total_warehouse=0
#     products={}
#     def __init__(self,name,price,quantity):
#         Warehouse.products[name]=Product(name,price,quantity)
#         Warehouse.total_warehouse+=1
#     @classmethod
#     def get_total_WH(cls):
#         return Warehouse.total_warehouse
#     def __add__(self, other):
#         return (self.products.update(other.products))
#     def __len__(self):
#         c=0
#         for i in self.products:
#             c+=1
#         return c
#     def __contains__(self, item):
#         return item in self.products
#
#     def __str__(self):
#         result = ""
#         for product in self.products.values():
#             result += str(product) + "\n"
#         return result
# w1=Warehouse('Laptop',55000,5)
# print(w1)


# '''7. Design:
#         • Abstract class MediaFile with play(), stop()
#         • Subclasses: MP3File, MP4File, WAVFile
#         • Private file path validation done internally
#         • A function start_player(media) that works with ANY object
#             that has play() (duck typing)
#             Demonstrate mixing true polymorphism + duck typing.'''
# class MediaFile(ABC):
#     # def __init__(self,path):
#     #     self.__path=path
#     @abstractmethod
#     def play(self):
#         print('Play')
#     @abstractmethod
#     def stop(self):
#         print('Stop')
#     def validation(self):
#         print('Validation')
# class MP3File(MediaFile):
#     def __init__(self,path):
#         try:
#         # self.validation(path)
#             self.path=self.__validation(path)
#         except ValueError:
#             print(' File Path is Incorrect')
#     def play(self):
#         print('MP3File_Player')
#     def stop(self):
#         print('MP3File_Stop')
#     def __validation(self,path):
#         if not path.endswith('.mp3'):
#             raise ValueError
#         return  path
# class WAVFile(MediaFile):
#     def __init__(self, path):
#         try:
#             # self.validation(path)
#             self.path = self.__validation(path)
#         except ValueError:
#             print(' File Path is Incorrect')
#     def play(self):
#         print('WAVFile_Player')
#     def stop(self):
#         print('WAVFile_Stop')
#     def __validation(self,path):
#         if not path.endswith('.wav'):
#             raise ValueError
#         return  path
# class MP4File(MediaFile):
#     def __init__(self, path):
#         try:
#             # self.validation(path)
#             self.path = self.__validation(path)
#         except ValueError:
#             print(' File Path is Incorrect')
#     def play(self):
#         print('MP4File_Player')
#     def stop(self):
#         print('MP4File_Stop')
#     def __validation(self,path):
#         if not path.endswith('.mp4'):
#             raise ValueError
#         return  path
# # k=MP3File('jhgf.mp3')
# k=MP3File('jhgf.mp4')
# def start_player(media):
#     media.play()
# def stop_player(media):
#     media.stop()
# start_player(k)


# ''' 8. Create:
#         • Abstract class StatementFormatter
#         • Subclasses: PDFFormatter, JSONFormatter, TextFormatter
#         • Overload __call__() so that formatters can be used like functions
#         • Overload __repr__ for debugging
#         • Demonstrate polymorphic behavior in a reporting pipeline '''
# class StatementFormatter(ABC):
#     @abstractmethod
#     def __call__(self):
#         pass
#     @abstractmethod
#     def __repr__(self):
#         pass
# class PDFFormatter(StatementFormatter):
#     def __call__(self):
#         print('PDFFormatter.__call__')
#     def __repr__(self):
#         return 'PDFFormatter.__repr__()'
# class JSONFormatter(StatementFormatter):
#     def __call__(self):
#         print("JSONFormatter.__call__")
#     def __repr__(self):
#         return 'JSONFormatter.__repr__()'
# class TextFormatter(StatementFormatter):
#     def __call__(self):
#         print("TextFormatter.__call__()")
#     def __repr__(self):
#         return 'TextFormatter.__repr__()'
# t1=TextFormatter()
# j1=JSONFormatter()
# p1=PDFFormatter()
# print(t1)
# l=[t1,j1,p1]
# def fun(x):
#     x()
#     print(x)
# for i in l:
#     fun(i)
# '''9. Classes:
#         • LightDevice
#         • SecurityDevice
#         • SmartCamera(LightDevice, SecurityDevice)
#       Requirements:
#         • Resolve method conflicts using MRO
#         • Encapsulate internal camera logs
#         • SmartCamera overrides both parents’ behaviors
#         • Use super() responsibly in multiple inheritance '''
# class Device(ABC):
#     @abstractmethod
#     def start(self):
#         print('Device started')
#     @abstractmethod
#     def stop(self):
#         print('Device stopped')
#     @abstractmethod
#     def mic_on(self):
#         print('Mic is On')
#     @abstractmethod
#     def mic_off(self):
#         print('Mic is Off')
#     @abstractmethod
#     def light_off(self):
#         print('Light is Off')
#     @abstractmethod
#     def light_On(self):
#         print('Light is On')
#     @abstractmethod
#     def shutter_off(self):
#         print('Shutter is Off')
#     @abstractmethod
#     def shutter_on(self):
#         print('Shutter is On')
#     @abstractmethod
#     def recorder_off(self):
#         print('Recorder is Off')
#     @abstractmethod
#     def recorder_on(self):
#         print('Recorder is On')
# class LightDevice(Device):
#     def LightDevice_on(self):
#         print('Light_Device  is On')
#     def LightDevice_off(self):
#         print('Light_Device  is Off')
#     def shutter_off(self):
#         super().shutter_off()
#         # super().shutter_off()
#     def light_off(self):
#         print('Light is Off')
#         super().light_off()
#     def light_On(self):
#         print('Light is On')
#         super().light_On()
#     def shutter_off(self):
#         print('Shutter is Off')
#         super().shutter_on()
#     def shutter_on(self):
#         super().shutter_off()
#         print('Shutter is On')
#     def mic_on(self):
#         super().mic_on()
#         print('Mic is On')
#     def mic_off(self):
#         super().mic_off()
#         print('Mic is Off')
#     def recorder_on(self):
#         super().recorder_on()
#         print('Recorder is On')
#     def recorder_off(self):
#         super().recorder_off()
#         print('Recorder is Off')
#     def shutter_off(self):
#         super().shutter_off()
#         print('Shutter is Off')
#     def shutter_on(self):
#         super().shutter_on()
#         print('Shutter is On')
# class SecurityDevice(Device):
#     def security_device_on(self):
#         print('SecurityDevice  is On')
#     def security_device_off(self):
#         print('SecurityDevice  is Off')
#     # @abstractmethod
#     def start(self):
#         print('Security Device started')
#     # @abstractmethod
#     def stop(self):
#         print('Security Device stopped')
#     # @abstractmethod
#     def mic_on(self):
#         print('Security Mic is On')
#     # @abstractmethod
#     def mic_off(self):
#         print(' Security Mic is Off')
#     # @abstractmethod
#     def light_off(self):
#         print('Security Light is Off')
#     # @abstractmethod
#     def light_On(self):
#         print('Security Light is On')
#     # @abstractmethod
#     def shutter_off(self):
#         print('Security Shutter is Off')
#     # @abstractmethod
#     def shutter_on(self):
#         print('Security Shutter is On')
#     # @abstractmethod
#     def recorder_off(self):
#         print('Security Recorder is Off')
#     # @abstractmethod
#     def recorder_on(self):
#         print('Security Recorder is On')
# class SmartCamera(LightDevice,SecurityDevice):
#     logs=0
#     def __init__(self):
#         # self.__logs=logs
#         SmartCamera.logs+=1
#     def start_camera(self):
#         super().LightDevice_on()
#         super().light_On()
#         super().mic_on()
#         super().recorder_on()
#         super().shutter_on()
#     def stop_camera(self):
#         super().LightDevice_off()
#         super().light_off()
#         super().mic_off()
#         super().recorder_off()
#         super().shutter_off()
#     def get_logs(self):
#         return SmartCamera.logs
#
# def fun1(x):
#     x.start_camera()
# # fun1(SmartCamera())
# def fun2(x):
#     x.stop_camera()
# fun1(SmartCamera())
# fun2(SmartCamera())
# print('Smart_Camera_Logs:',SmartCamera().get_logs())

# '''10. Create:
#         • Abstract class MenuItem with get_price()
#         • Subclasses: Pizza, Burger, Drink
#         • Order class containing a list of items (composition)
#         • Encapsulate the list internally
#         • Override methods to apply custom pricing logic for each food type '''
# class Menuitem(ABC):
#     @abstractmethod
#     def get_price(self):
#         pass
# class Pizza(Menuitem):
#     def get_price(self):
#         print('Pizza')
#     def __str__(self):
#         return 'Pizza'
# class Burger(Menuitem):
#     def get_price(self):
#         print('Burger')
#     def __str__(self):
#         return 'Burger'
# class Drink(Menuitem):
#     def get_price(self):
#         print('Drink')
#     def __str__(self):
#         # print(1)
#         return 'Drink'
# class Order:
#     def __init__(self,l):
#         self.__items=l
#     def __iter__(self):
#         self.i=0
#         return self
#     def __next__(self):
#         self.i+=1
#         if self.i-1<len(self.__items):
#             return self.__items[self.i-1]
#         else:
#             raise StopIteration
#     def __str__(self):
#         return f'{self.__items}'
# o1=Order([Pizza(),Burger(),Drink()])
# for i in o1:
#     print(i)

# '''11. Create:
#         • Class Applicant with private skills list
#         • Overload:
#                 o + to add skill
#                 o - to remove skill
#                 o == to compare applicants who have identical skill sets
#         • Use inheritance to create ExperiencedApplicant with additional fields'''
# class Applicant(ABC):
#     def __init__(self,name,l):
#         self.__skills=l
#         self.name=name
#     def __add__(self, *other):
#         other=list(other)
#         return self.__skills.extend(other)
#
#         if len(other)==1:
#             return self.__skills.extend(other)
#         else:
#             return self.__skills.extend(other)
#     def get_skills(self):
#         return self.__skills.copy()
#     def __sub__(self, other):
#         if other in self.__skills:
#             self.__skills.remove(other)
#         else:
#             raise ValueError
#     def __eq__(self, other):
#         k=set(self.__skills)
#         k1=set(other.__skills)
#         return k==k1
#     def __str__(self):
#         return (f'Name={self.name}\n'
#                 f'Skills:{self.get_skills()}')
# class ExperiencedApplicant(Applicant):
#     def __init__(self,name,l,experience,current_role,company):
#         self.experience=experience
#         self.current_role=current_role
#         self.company=company
#         super().__init__(name,l)
#     def __str__(self):
#         return (f'Name:{self.name}\n'
#                 f'Skills:{self.get_skills()}\n'
#                 f'Experience: {self.experience}\n'
#                 f'Current_Role: {self.current_role}\n'
#                 f'Company: {self.company}\n')
# a1=Applicant('Aadhya',['Python','Java','SQL'])
# a2=Applicant('Paaru',['Python','Java_Script','My_SQL'])
# a3=Applicant('satwik',['C','Java','Postgre_SQL'])
# a1+'Pycharm'
# print(a1.get_skills())
# a1-'SQL'
# print(a1.get_skills())
# print(a1==a2)
# print(a3==a2)
# ea1=ExperiencedApplicant('Aadhi',['Python','Java'],2,'Developer','Net_cracker')
# ea2=ExperiencedApplicant('Shiva',['Python_Oops','Java_Script'],2,'Developer','Net_cracker')
# print(ea1)
# print(a1)
# ea2+'Python'
# print(ea2.get_skills())
# print(ea2)



''' 12. Create: 
        • Character → base class 
        • Warrior, Archer, Mage subclasses 
     Each subclass: 
        • Overrides attack() 
        • Encapsulates health with @property 
        • Prevents negative HP 
        • Uses class attributes for shared attributes (e.g., stamina_cost)
    Demonstrate polymorphic combat simulation. '''
class Character(ABC):
    def __init__(self):
        self.__HP=100
    @abstractmethod
    @property
    def get_health(self):
        return self.__HP
    @get_health.setter
    def get_health(self,k):
        if k+self.__HP>=100:
            self.__hp=100

        self.__HP-=k


    def attack(self):
        pass
    @abstractmethod
    def
    # @abstractmethod



'''13. Build: 
        • Transport abstract class 
        • Subclasses: Taxi, Bus, Train 
        • Each implements: o calculate_fare() differently 
        • Use static method to validate distance 
        • Encapsulate fare state 
        • Add class method to update government tax slab '''
'''14. Design: 
        • Abstract class Model with train(), predict() 
        • Implement LinearRegressionModel and DecisionTreeModel(just print or write a logic, 
                focus on calling and concept) 
        • A Pipeline class that: 
            o Accepts any model 
            o Uses composition to chain transformations 
            o Overloads __call__() to run predictions 
        • Encapsulates internal steps'''
''' 15. Classes: 
        • User Create a mini version of Amazon with: 
        • Product 
        • Seller(User) 
        • Buyer(User) 
        • Order 
        • Cart Requirements (must use all OOP concepts):
                >Inheritance: Seller and Buyer extend User 
                >Encapsulation: protect internal cart list, user password 
                >Abstraction: base class User defines abstract get_role() 
                >Polymorphism: different users behave differently in checkout 
                >Composition: Buyer “has” a Cart 
                >Operator overloading: 
                        • + to add product to Cart 
                        • - to remove product 
                >Properties: validate product price 
                >Class methods: tracking total users 
                >Static methods: validating product IDs 
                >__str__ for readable summaries 
                >MRO behavior when Buyer inherits from multiple mixins (e.g., RewardsMixin) '''



#from abc import ABC, abstractmethod
# class User(ABC):
#     total_users = 0
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#         self.total_users += 1
#     @abstractmethod
#     def get_role(self):
#         pass
#     @classmethod
#     def get_total_users(cls):
#         return cls.total_users
#
# class Product:
#     def __init__(self, name, price):
#         self.name = name
#         self.price = price
#     def __repr__(self):
#         return f'Product({self.name}, {self.price})'
#     def __str__(self):
#         return f'Product({self.name}, {self.price})'
#
# class Seller(User):
#     def __init__(self, name, age):
#         super().__init__(name, age)
#     def get_role(self):
#         return "seller"
# class Buyer(User):
#     def __init__(self, name, age, cart):
#         super().__init__(name, age)
#         self.cart = cart
#     def get_role(self):
#         return "buyer"
#     def  checkout(self):
#         print(f"{self.cart.get_totalprice()} is the total price")
# class Order:
#     def __init__(self, product, quantity):
#         self.product = product
#         self.quantity = quantity
#
# class Reward:
#     def get_totalprice(self, tp):
#         if tp > 1000:
#             return tp*0.9
#         return tp
#
#
#
# class Cart(Reward):
#     def __init__(self):
#         self.__cart = []
#     def __add__(self, other):
#         self.__cart.append(other)
#     def __sub__(self, other):
#         self.__cart.remove(other)
#     def get_cart(self):
#         return self.__cart.copy()
#     def get_totalprice(self):
#         tp=0
#         for i in self.__cart:
#             tp+=i.price
#         return super().get_totalprice(tp)
#
#     def checkout(self,role,total_price):
#         if role == "seller":
#             print(f"Checkout with price {total_price} received")
#         else:
#             print(f"Checkout with price {total_price} paid")
#
# def checkout(user,cart):
#     total_price = cart.get_totalprice()
#     cart.checkout(user.get_role(),total_price)
#
#
# product=Product("laptop", 100)
# c=Cart()
# c+product
# p=Product("AC", 300)
# c+p
# print(c.get_cart())
# print(c.get_totalprice())
# u2=Buyer("B", 30,c)
# u2.checkout()
#
#
# #2
# class StatementFormatter(ABC):
#
#     def __format(self):
#         print("Formatting statement")
#     @abstractmethod
#     def call_formatter(self):
#         self.__format()
#
# class JSONFormatter(StatementFormatter):
#     def call_formatter(self):
#         print("Formatting JSON")
#         super().call_formatter()
#     def __call__(self, text):
#         self.call_formatter()
#         print(f"text formatted to json: {text}")
#     def __repr__(self):
#         return "JSONFormatter()"
# l=[JSONFormatter()]
# for i in l:
#     print(i)
#     i("hello everyone")


