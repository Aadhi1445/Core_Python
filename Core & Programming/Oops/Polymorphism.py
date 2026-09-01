'''Q1. Create a class Animal with make_sound() and derived classes Dog, Cat, Cow that override it.
Demonstrate polymorphism by iterating over a list of different animal objects and calling make_sound(). '''
class Animal:
    def sound(self):
        print("Animal Makes sound")
class Dog(Animal):
    def sound(self):
        print("Dog Makes 'Bow! Bow!'")
class Cat(Animal):
    def sound(self):
        print("Cat Makes 'Meow! Meow!'")
class Cow(Animal):
    def sound(self):
        print("Cow Makes 'Amba..! Amba..!'")

Dog1=Dog()
Cat1=Cat()
Cow1=Cow()
l=[Dog1,Cat1,Cow1]
for i in l:
    i.sound()
print('-'*50)
'''Q2. Write a function operate(device) that calls device.start(). 
Pass in objects of Car, Computer, and WashingMachine — all of which define a start() method, 
but share no inheritance relationship. 
Show that Python’s polymorphism works through behavior, not type. '''
class Car:
    def start(self):
        print('Press Ignition button')
class Computer:
    def start(self):
        print('Press start button')
class Washing_machine:
    def start(self):
        print('Press Power On button')
def operate(device):
    device.start()
operate(Car())
operate(Computer())
operate(Washing_machine())
print('-'*50)
'''Q3. Create a Vector class that supports: 
• + operator → add coordinates 
• == operator → compare equality Show how operator overloading 
gives natural polymorphism to user-defined classes.'''
class Vector:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def __add__(self, other):
        return Vector(self.x+other.x,self.y+other.y)
    def __eq__(self, other):
        return self.x==other.x and self.y==other.y
    def __str__(self):
        return f'X:{self.x} Y:{self.y}'
v1=Vector(2,3)
v2=Vector(4,6)
v3=Vector(3,1)
v4=Vector(3,1)
print(v1+v2)
print(v1+v2+v3)
print(v1==v2)
print(v4==v3)
print('-'*50)
'''Q4. Create a base class Transport with move() and 
derived classes Bus and Bike that override it but also call the parent implementation using super(). 
Show the combination of reuse + custom behavior.'''
class Transport:
    def move(self):
        print("Transport")
class Bus(Transport):
    def move(self):
        super().move()
        print("Bus")
class Bike(Transport):
    def move(self):
        super().move()
        print('Bike')
b=Bike()
bus=Bus()
b.move()
bus.move()
print('-'*50)
'''Q5. Using the abc module, create an abstract class Notification with send(). 
Implement subclasses EmailNotification, SMSNotification, PushNotification — each with its own send() logic. 
Demonstrate polymorphism by looping over all and calling send().'''


'''Q6. Design: 
• Base class Payment with process(amount) 
• Subclass CreditCardPayment adds process(amount, card_type) 
Demonstrate what happens when overriding with different signatures and how Python handles it.'''
class Payment:
    def process(self,amount):
        print('amount')
class Credit_card_Payment(Payment):
    def process(self,amount,card_type):
        print('Credit_payment')
        super().process(amount)
p=Payment()
p.process(3445)
c=Credit_card_Payment()
c.process(3434,'Platinum')
print('-'*50)
'''Q7. Create:
• Class Sorter with change(strategy) method.
Separate strategy  classes: BS, MS, QS, each implementing a different logic method.
Demonstrate how polymorphism can be achieved without inheritance by using'''

class BS:
    def logic(self,data):
        print('Bs:',data)
class MS:
    def logic(self,data):
        print('MS:',data)
class QS:
    def logic(self,data):
        print('QS:',data)
class Sorter:
    # print('dfg')
    def change(self,strategy):
        self.strategy=strategy
        # print(self.strategy)
    def sort(self,data):
        self.strategy.logic(data)
# Sorter().change('bs')
s1=Sorter()
# s1.change('BS') --> we are sending an string object
# s1.change(BS)# --> we are sending an class object itself so  sort requires two arguments  i.e. self,'ghj' but here only 'ghj is going to self what about data arguments
# s1.sort('dfgh')
s1.change(BS())
s1.sort('ghj')
s1.change(MS())
s1.sort('ghj')
s1.change(QS())
s1.sort('ghj')
print('-'*50)
'''Q8. Create:
• Base Account → withdraw()
• Subclass SavingsAccount → modifies withdraw()
• Subclass PremiumSavingsAccount → overrides again but
calls parent using super() Show how polymorphism works across multiple levels.'''
class Account:
    def __init__(self,balance=0):
        self.balance=balance
    def withdraw(self):
        print('Account  class withdraw')
        # if amount<=self.balance and amount>0:
        #     self.balance-=amount
        #     return self.balance
        # else:
        #     return "Invalid Amount"
class SavingsAcc(Account):
    def withdraw(self):
        print('SavingsAcc  class withdraw')
        super().withdraw()
class PremiumSavingsAcc(SavingsAcc):
    def withdraw(self):
        print('PremiumSavingsAccount  class withdraw')
        super().withdraw()
p1=PremiumSavingsAcc()
p1.withdraw()
print('-'*50)
''' Q9.
Create a function draw(shape) that works for objects of classes Circle, Square, and Rectangle,
each implementing a draw() method.
Add another unrelated class Car with draw() and pass it — what happens and why? '''
def draw(shape):
    shape.draw()
class Shape:
    pass
class Circle(Shape):
    def draw(self):
        print("Circle's draw")
class Square(Shape):
    def draw(self):
        print(" Square's Draw")
class Rectangle(Shape):
    def draw(self):
        print("Rectangle's Draw")
class Car:
    def draw(self):
        print('Car"s Draw')
l=[Square(),Circle(),Rectangle(),Car()]
for i in l:
    draw(i)
print('-'*50)
'''Q10. Design a polymorphic system for payment handling (UPI, Card, Cash) — all have a pay() method.
Now implement a version that checks types explicitly using isinstance() before calling pay().
Compare both designs and explain why one breaks the spirit of polymorphism.'''
class UPI:
    def pay(self):
        print('UPI')
class Card:
    def pay(self):
        print('Card')
class Cash:
    def pay(self):
        print("Cash")
def check(k):
    if isinstance(k,UPI):
        k.pay()
    elif isinstance(k,Cash):
        k.pay()
    elif isinstance(k,Card):
        k.pay()
check(UPI())
check(Card())
check(Cash())
