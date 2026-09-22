from abc import ABC,abstractmethod
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

# '''12. Design an abstract class PaymentGateway with:
#     • authenticate()
#     • pay(amount)
#     • refund(amount)
#     Implement subclasses:
#         • UPIPayment
#         • CardPayment
#         • NetBankingPayment
#         Show how abstraction helps your main program call payment
#                 methods without caring about the payment type.'''
# class PaymentGateway(ABC):
#     @abstractmethod
#     def authenticate(self):
#         print('Aunthentication Succesfull ')
#     @abstractmethod
#     def pay(self,amount):
#         print('Debited')
#     @abstractmethod
#     def refund(self,amount):
#         print('Refund')
# class UPI(PaymentGateway):
#     def authenticate(self):
#         super().authenticate()
#     def pay(self,amount):
#         super().pay(amount)
#     def refund(self,amount):
#         super().refund(amount)
# class Card(PaymentGateway):
#     def authenticate(self):
#         super().authenticate()
#     def pay(self,amount):
#         super().pay(amount)
#     def refund(self,amount):
#         super().refund(amount)
# class NetBanking(PaymentGateway):
#     def authenticate(self):
#         super().authenticate()
#     def pay(self,amount):
#         super().pay(amount)
#     def refund(self,amount):
#         super().refund(amount)
# def fun(method,amount):
#     method.authenticate()
#     method.refund(amount)
#     method.pay(amount)
# k=fun(UPI(),500)
# print(k)
# # ph=UPI()
# # ph.authenticate()
# # ph.pay(1000)
# # ph.refund(500)
# '''13. Create:
#     • Abstract class VehicleControl with methods accelerate(), brake(), steer()
#     • Implement CarControl, BikeControl, TruckControl
#             Demonstrate calling each through a single interface.'''
# class VehicleControl(ABC):
#     @abstractmethod
#     def accelerate(self):
#         pass
#     @abstractmethod
#     def brake(self):
#         pass
#     @abstractmethod
#     def steer(self):
#         pass
# print(VehicleControl.__abstractmethods__)
# class CarControl(VehicleControl):
#     def accelerate(self):
#         print('CarControl ---Acceleration')
#     def brake(self):
#         print('CarControl ---Brake')
#     def steer(self):
#         print(' CarControl ---steer')
# c1=CarControl()
# print(CarControl.__abstractmethods__)
# class BikeControl(VehicleControl):
#     def accelerate(self):
#         print('BikeControl ---Acceleration')
#     def brake(self):
#         print('BikeControl ---Brake')
#     def steer(self):
#         print(' BikeControl ---steer')
# c1=BikeControl()
# print(BikeControl.__abstractmethods__)
# class TruckControl(VehicleControl):
#     def accelerate(self):
#         print('TruckControl ---Acceleration')
#     def brake(self):
#         print('TruckControl ---Brake')
#     def steer(self):
#         print(' TruckControl ---steer')
# c1=TruckControl()
# print(TruckControl.__abstractmethods__)
# '''14. Create an abstract class DatabaseDriver with:
#     • connect()
#     • execute(query)
#     • close()
#     Implement concrete drivers:
#         • MySQLDriver
#         • PostgresDriver
#         • SQLiteDriver
#         Show how abstraction helps
#             switch databases without rewriting main code.'''
# class DataBaseDriver(ABC):
#     @abstractmethod
#     def connect(self):
#         pass
#     @abstractmethod
#     def execute(self,querry):
#         pass
#     @abstractmethod
#     def close(self):
#         pass
# print(DataBaseDriver.__abstractmethods__)
# class MySqlDriver(DataBaseDriver):
#     def connect(self):
#         print('Connect -- MySqlDriver')
#     def execute(self,querry):
#         print(f'{querry} is executed')
#     def close(self):
#         print(' MySqlDriver --Closed')
# print(MySqlDriver.__abstractmethods__)
# class Postgresql(DataBaseDriver):
#     def connect(self):
#         print('Connect -- Postgresql')
#     def execute(self,querry):
#         print(f'{querry} is executed')
#     def close(self):
#         print(' Postgresql --Closed')
# print(Postgresql.__abstractmethods__)
# class SqlLiteDriver(DataBaseDriver):
#     def connect(self):
#         print('Connect -- SqlLiteDriver')
#     def execute(self,querry):
#         print(f'{querry} is executed')
#     def close(self):
#         print(' SqlLiteDriver --Closed')
# print(SqlLiteDriver.__abstractmethods__)
# def driver(db,querry):
#     db.connect()
#     db.execute(querry)
#     db.close()
# driver(SqlLiteDriver(),'Select* from table')
# '''15. Design a class ReportGenerator (abstract) with:
#     • load_data()
#     • process()
#     • export()
#     Implement:
#         • PDFReport
#         • ExcelReport
#         Demonstrate how abstraction enforces a multi-step structure.'''
# class ReportGenerator(ABC):
#     @abstractmethod
#     def load_data(self):
#         pass
#     @abstractmethod
#     def process(self):
#         pass
#     @abstractmethod
#     def export(self):
#         pass
# class PDFReport(ReportGenerator):
#     def load_data(self):
#         print('Load_data -- PDFReport')
#     def process(self):
#         print('Processed by PDFReport')
#     def export(self):
#         print('Exported by PDFReport')
# class ExcelReport(ReportGenerator):
#     def load_data(self):
#         print('Load_data -- ExcelReport')
#     def process(self):
#         print('Processed by ExcelReport')
#     def export(self):
#         print('Exported by ExcelReport')
# e1=ExcelReport()
# # e1.process()
# # e1.load_data()
# # e1.export()
# p1=PDFReport()
# # p1.process()
# # p1.load_data()
# # p1.export()
# def report(type):
#     type.load_data()
#     type.process()
#     type.export()
# report(e1)
# '''16. Create an abstract class RobotCommand with:
#     • execute()
#     • undo()
#     Implement:
#         • PickCommand
#         • PlaceCommand
#         • MoveCommand
#         Demonstrate how abstraction cleanly represents
#                 commands without revealing details.'''
# class RobotCommand(ABC):
#     @abstractmethod
#     def execute(self):
#         pass
#     @abstractmethod
#     def undo(self):
#         pass
# class PickCommand(RobotCommand):
#     def execute(self):
#         print('Pickup command by execute method')
#     def undo(self):
#         print('Undo the PickupCommand')
# class PlaceCommand(RobotCommand):
#     def execute(self):
#         print('placeCommand is executed.')
#     def undo(self):
#         print('Undo the placeCommand')
# class MoveCommand(RobotCommand):
#     def execute(self):
#         print('MoveCommand is executed')
#     def undo(self):
#         print('MoveCommand is undo')
# def run_command(command):
#     command.execute()
#     command.undo()
# pick = PickCommand()
# place = PlaceCommand()
# move = MoveCommand()
# run_command(pick)
# run_command(place)
# run_command(move)
'''17. Create an abstract class MLModel with:
    • train(data)
    • predict(x)
    • evaluate(test_set)
        Implement models:
            • LinearRegressionModel- some different logic
            • DecisionTreeModel – some logic Show how a generic training
                loop works for any model without caring about details.'''





'''18. Design a system without abstraction first:
    • Write separate functions for EmailSender, SMSSender, PushSender
        Show how the main program becomes a mess with constant if/else.
    Then:
        • Redesign using an abstract base class Notifier.'''







'''19. Create an abstract MediaPlayer with:
        • load()
        • play()
        • stop()
    Implement:
        • MP3Player
        • WAVPlayer
        • AACPlayer 
        Demonstrate calling each via a unified interface.'''
class MediaPlayer(ABC):
    @abstractmethod
    def load(self):
        pass
    @abstractmethod
    def play(self):
        pass
    @abstractmethod
    def stop(self):
        pass
class Mp3Player(MediaPlayer):
    def load(self):

        pass




'''20. Design:
    • Abstract base class Sensor with functions read_value() and calibrate()
    • Subclasses:
        TemperatureSensor, PressureSensor, HumiditySensor Encapsulate:
    • internal raw sensor readings
    • calibration factor Hide all raw operations and allow only a public, clean get_reading() method.'''
# ##12. Design an abstract class PaymentGateway with: • authenticate() • pay(amount) • refund(amount) Implement subclasses: • UPIPayment • CardPayment • NetBankingPayment Show how abstraction helps your main program call payment methods without caring about the payment type. ##
#
# from abc import ABC ,abstractmethod
# class PaymentGateway(ABC):
#     @abstractmethod
#     def authenticate(self):
#         pass
#     @abstractmethod
#     def pay(self,amount):
#         pass
#     @abstractmethod
#     def refund(self,amount):
#         pass
# class UPI(PaymentGateway):
#     def __init__(self,amount):
#         self.amount = amount
#     def authenticate(self):
#         # if pin=="93910":
#         print("you can make payment")
#
#     def pay(self,amount):
#         self.amount -= amount
#     def refund(self,amount):
#         self.amount += amount


# class CardPayment(PaymentGateway):
#     def __init__(self,amount):
#         self.amount = amount
#     def authenticate(self,pin):
#         if pin=="93910":
#             print("you can make payment")
#
#     def pay(self,amount):
#         self.amount -= amount
#     def refund(self,amount):
#         self.amount += amount
#
# class NetBanking(PaymentGateway):
#     def __init__(self,amount):
#         self.amount = amount
#     def authenticate(self,pin):
#         if pin=="93910":
#             print("you can make payment")
#
#     def pay(self,amount):
#         self.amount -= amount
#     def refund(self,amount):
#         self.amount += amount
#
# def process_payment(PaymentGateway,amount):
#     PaymentGateway.authenticate()
#     PaymentGateway.refund(amount)
#     PaymentGateway.pay(amount)
#
# k=UPI(100)
# process_payment(k,100)
# print(k.amount)