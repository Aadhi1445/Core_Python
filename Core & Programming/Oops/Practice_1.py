from abc import ABC,abstractmethod
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
#             print('Insufficient funds')
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
#         interest= amount+(0.3*amount)
#         return (f'{interest} for {amount} in Savings_Account\n'
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
# fd=Fixed_Deposit('1444100638',5000)
# print(fd.get_balance())
# # fd.deposit(3000)
# fd.cal_interest(100)






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
'''4. Create classes: 
    • Person → base 
        • MedicalStaff(Person) 
        • Doctor(MedicalStaff) 
        • Surgeon(Doctor) 
    Requirements: 
        • Hide sensitive data (e.g., salary, patient notes) 
        • Abstract method perform_duty() 
        • Each level overrides the method with more specific behavior 
        • Use super() to chain constructor calls Demonstrate consistency across hierarchy.'''
class Person(ABC):
    def __init__(self,name):
        self.__p_name=name
    @abstractmethod
    def person_duty(self):
        print('Taking Medicine')
class MedicalStaff(Person):
    def __init__(self,name):
        self.__s_name=name
    def person_duty(self):
        print('Medical_Staff duties')
class Doctor(MedicalStaff):
    def __init__(self,name):
        pass






'''5. Classes: • User • Instructor(User) • Student(User) • TeachingAssistant(Student, Instructor) Requirements: • Track course assignments privately • Ensure TAs override submit_work() and grade_work() • Print MRO and explain how Python resolves conflicts 6. Create: • Product class with private price and quantity • Warehouse class containing multiple products • Overload: o + to merge warehouses o len() to return number of unique products o in operator to check if product exists • Provide class method to track total warehouses created 7. Design: • Abstract class MediaFile with play(), stop() • Subclasses: MP3File, MP4File, WAVFile • Private file path validation done internally • A function start_player(media) that works with ANY object that has play() (duck typing) Demonstrate mixing true polymorphism + duck typing. 8. Create: • Abstract class StatementFormatter • Subclasses: PDFFormatter, JSONFormatter, TextFormatter • Overload __call__() so that formatters can be used like functions • Overload __repr__ for debugging • Demonstrate polymorphic behavior in a reporting pipeline 9. Classes: • LightDevice • SecurityDevice • SmartCamera(LightDevice, SecurityDevice) Requirements: • Resolve method conflicts using MRO • Encapsulate internal camera logs • SmartCamera overrides both parents’ behaviors • Use super() responsibly in multiple inheritance 10. Create: • Abstract class MenuItem with get_price() • Subclasses: Pizza, Burger, Drink • Order class containing a list of items (composition) • Encapsulate the list internally • Override methods to apply custom pricing logic for each food type 11. Create: • Class Applicant with private skills list • Overload: o + to add skill o - to remove skill o == to compare applicants who have identical skill sets • Use inheritance to create ExperiencedApplicant with additional fields 12. Create: • Character → base class • Warrior, Archer, Mage subclasses Each subclass: • Overrides attack() • Encapsulates health with @property • Prevents negative HP • Uses class attributes for shared attributes (e.g., stamina_cost) Demonstrate polymorphic combat simulation. 13. Build: • Transport abstract class • Subclasses: Taxi, Bus, Train • Each implements: o calculate_fare() differently • Use static method to validate distance • Encapsulate fare state • Add class method to update government tax slab 14. Design: • Abstract class Model with train(), predict() • Implement LinearRegressionModel and DecisionTreeModel(just print or write a logic, focus on calling and concept) • A Pipeline class that: o Accepts any model o Uses composition to chain transformations o Overloads __call__() to run predictions • Encapsulates internal steps 15. Classes: • User Create a mini version of Amazon with: • Product • Seller(User) • Buyer(User) • Order • Cart Requirements (must use all OOP concepts): >Inheritance: Seller and Buyer extend User >Encapsulation: protect internal cart list, user password >Abstraction: base class User defines abstract get_role() >Polymorphism: different users behave differently in checkout >Composition: Buyer “has” a Cart >Operator overloading: • + to add product to Cart • - to remove product >Properties: validate product price >Class methods: tracking total users >Static methods: validating product IDs >__str__ for readable summaries >MRO behavior when Buyer inherits from multiple mixins (e.g., RewardsMixin) '''