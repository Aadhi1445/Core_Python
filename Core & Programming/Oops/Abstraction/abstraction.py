# from abc import ABC,abstractmethod
# class Car(ABC):
#     @abstractmethod
#     def wheels(self):
#         print('Wheels')
#     def name():
#         return f'name'
# # c1=Car()
# print(Car.__abstractmethods__)
# class Ferrari(Car):
#     def wheels(self):
#         print('Ferrari')
#         print(45678)
#     @abstractmethod
#     def steering(self):
#         pass
#         # print(1)
# print(Ferrari.__abstractmethods__)
# # f1=Ferrari()
# class Ferrari_12(Ferrari):
#     # pass
#     def steering(self):
#         pass
# f1=Ferrari_12()
# # f1=Ferrari()
# print(Ferrari_12.__abstractmethods__)
from abc import ABC,abstractmethod
# '''11. Using abc module:
#         • Create an abstract class Shape with area(), perimeter()
#         • Implement Circle, Rectangle, Triangle Demonstrate:
#         • why base class should NOT contain calculation logic
#         • what happens if a subclass fails to implement one of the methods'''
# class Shape(ABC):
#     @abstractmethod
#     def area(self):
#         print('Area')
#     @abstractmethod
#     def perimeter(self):
#         print('Perimeter')
# # print(Shape.__abstractmethods__)
# class Circle(Shape):
#     def __init__(self,r):
#         self.radius=r
#     def area(self):
#         return (1//2*(22/7)*self.radius*self.radius)
#         # super().area()
#     def perimeter(self):
#         return (2*(22/7)*self.radius*self.radius)
#         # super().perimeter()
# # print(Circle.__abstractmethods__)
# class Triangle(Shape):
#     def __init__(self,a,b,c,h):
#         self.a=a
#         self.b=b
#         self.c=c
#         self.height=h
#     def area(self):
#         return (1//2*(self.b*self.h))
#         # super().area()
#     def perimeter(self):
#         return (self.a+self.b+self.c)
#         # super().perimeter()
# # print(Triangle.__abstractmethods__)
# class Rectangle(Shape):
#     def __init__(self,l,b):
#         self.length=l
#         self.breadth=b
#     def area(self):
#         return (self.length*self.breadth)
#         # super().area()
#     def perimeter(self):
#         return  (2*(self.length+self.breadth))
#         # super().perimeter()
# # print(Rectangle.__abstractmethods__)
# r1=Rectangle(20,10)
# print(r1.area())
# print(r1.perimeter())

'''12. Design an abstract class PaymentGateway with:
    • authenticate()
    • pay(amount)
    • refund(amount) 
    Implement subclasses:
        • UPIPayment 
        • CardPayment
        • NetBankingPayment 
        Show how abstraction helps your main program call payment
                methods without caring about the payment type.'''
class PaymentGateway(ABC):
    @abstractmethod
    def authenticate(self):
        print('Aunthentication Succesfull ')
    @abstractmethod
    def pay(self,amount):
        print('Debited')
    @abstractmethod
    def refund(self,amount):
        print('Refund')
class UPI(PaymentGateway):
    def authenticate(self):
        super().authenticate()
    def pay(self,amount):
        super().pay(amount)
    def refund(self,amount):
        super().refund(amount)
ph=UPI()
ph.authenticate()
ph.pay(1000)
ph.refund(500)
'''13. Create:
    • Abstract class VehicleControl with methods accelerate(), brake(), steer()
    • Implement CarControl, BikeControl, TruckControl
            Demonstrate calling each through a single interface.
14. Create an abstract class DatabaseDriver with:
    • connect()
    • execute(query)
    • close() Implement concrete drivers:
    • MySQLDriver
    • PostgresDriver
    • SQLiteDriver Show how abstraction helps
        switch databases without rewriting main code.
15. Design a class ReportGenerator (abstract) with:
    • load_data()
    • process()
    • export()
    Implement:
    • PDFReport
    • ExcelReport
    Demonstrate how abstraction enforces a multi-step structure.
16. Create an abstract class RobotCommand with:
    • execute()
    • undo()
    Implement:
        • PickCommand
        • PlaceCommand
        • MoveCommand Demonstrate how abstraction cleanly represents
                commands without revealing details.
17. Create an abstract class MLModel with:
    • train(data)
    • predict(x)
    • evaluate(test_set)
        Implement models:
            • LinearRegressionModel- some different logic
            • DecisionTreeModel – some logic Show how a generic training
                loop works for any model without caring about details.
18. Design a system without abstraction first:
    • Write separate functions for EmailSender, SMSSender, PushSender
        Show how the main program becomes a mess with constant if/else.
    Then:
        • Redesign using an abstract base class Notifier.
19. Create an abstract MediaPlayer with:
        • load()
        • play()
        • stop()
    Implement:
        • MP3Player
        • WAVPlayer
        • AACPlayer Demonstrate calling each via a unified interface.
20. Design:
    • Abstract base class Sensor with functions read_value() and calibrate()
    • Subclasses:
        TemperatureSensor, PressureSensor, HumiditySensor Encapsulate:
    • internal raw sensor readings
    • calibration factor Hide all raw operations and allow only a public, clean get_reading() method.'''