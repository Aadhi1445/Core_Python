'''Create a Vehicle Class:
        . car,bike,auto subclasses
        . a driver class that contains a vehicle
        . a ride class that:
            calculates fare differently depending on the type of vehicle
        . stores drivers+vehicles combination
        . protects internal fare formula
        also:
            use __str__ to print readable ride summaries'''
class Vehicle:
    def __str__(self):
        return 'Ride is booked'
class Car(Vehicle):
    def __fare(self):
        k = input('Enter type of transport: ')
        km = int(input('Enter Distance in "km" : '))
        amount=30*km
        return amount

class Bike(Vehicle):
    def __fare(self):
        k = input('Enter type of transport: ')
        km = int(input('Enter Distance in "km" : '))
        amount=30*km
        return amount
class Auto(Vehicle):
    def __fare(self):
        k = input('Enter type of transport: ')
        km = int(input('Enter Distance in "km" : '))
        amount=30*km
        return amount
class Driver(Vehicle):
    pass

class Ride():
    def __fare(self,obj,km):
        obj.__fare(km)

r1=Ride()
r1.fare()





'''
classes :
 * Light device * security device
 *smartcamera(light device , security device)
 Requirements:
        *resolve method conflicts using mro
        * encapsulate internal cmaera logs
        * smart camera overrides both parent behaviours
        * use super() responsibly in multiple inheritance
'''
from  abc import ABC,abstractmethod
class Light_Device(ABC):
    @abstractmethod
    def turn_on(self):
        super().turn_on()
        print('Light is turned ON ')
    @abstractmethod
    def turn_off(self):
        super().turn_off()
        print('Light is Turned OFF ')
    @abstractmethod
    def Shutter(self):
        print('Shutter is adjusted')
    @abstractmethod
    def record(self):
        super().record()
        print('Started Recording')
class Security_Device(ABC):
    @abstractmethod
    def turn_on(self):
        print('Security System is turned ON ')
    @abstractmethod
    def turn_off(self):
        print('Security System  is Turned OFF ')
    @abstractmethod
    def record(self):
        print('Security System is Turned ON while Started Recording')
class Smart_Camera(Light_Device,Security_Device):
    log=[]
    def __init__(self):
        self.__Logs='Log'
        Smart_Camera.log.append(self.__Logs)
    @classmethod
    def camera_logs(cls):
        return cls.__logs
    def turn_off(self):
        super().turn_off()
    def turn_on(self):
        super().turn_on()
    def record(self):
        super().record()
    def Shutter(self):
        super().Shutter()
s1=Smart_Camera()
s2=Smart_Camera()
# print(Smart_Camera.log)
def camera(x):
    x.turn_on()
    x.Shutter()
    x.record()
    x.turn_off()
camera(s2)




