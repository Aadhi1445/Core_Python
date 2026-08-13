class User:
    def __init__(self,n,a,g,dob):
        self.name=n
        self.age=a
        self.gender=g
        self.dob=dob
    def login(self):
        print('Successfully Logged in')
    def logout(self):
        print('successfully logged out')
print(User.mro())
class Instagram(User):
    def post(self):
        print(f'{self.name} post')
        print('got 1l likes')
a1=Instagram('parul',15,'Male','23-07-2004')
a1.post()
a1.login()
a1.logout()
print(Instagram.mro())
print('-'*50)
class Restaurants:
    def __next__(self,n,r,add):
        self.name=n
        self.rating=r
        self.address=add
    def display_menu(self):
        print('All Dishes are non-veg only')
class Swiggy(User,Restaurants):
    def display(self):
        print(f'Name:{self.name}\n'
              f'Age:{self.age}\n'
              f'Gender:{self.gender}\n'
              f'Dob:{self.dob}')
    def display(self):
        print('user"s details')
print(Swiggy.mro())
class Zomato(User,Restaurants):
    def display(self):
        print('Zomato')
print(Zomato.mro())
class Customer(Swiggy,Zomato):
    def order(self):
        print('Just Ordered')
c1=Swiggy('Parul',35,'Male','23-07-2004')
c1.display()
print(Customer.mro())
print('-'*50)
class Bank(User):
    Name='RBI'
    def guide_lines(self):
        print('Beware of Scammer and Call 0004')
class Bhim_UPI(Bank,Swiggy):
    def Payments(self,amount):
        print(f'{self.amount} has been paid through UPI')
b1=Bhim_UPI('Shiva',21,'male','11-09-2004')
b1.display()
print(Bhim_UPI.mro())
print('-'*50)

