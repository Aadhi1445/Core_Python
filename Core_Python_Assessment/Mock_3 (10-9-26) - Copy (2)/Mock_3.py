# '''Question-1'''
# class A:
#     def display(self):
#         print('A class')
# class B(A):
#     def display(self):
#         print('B class')
#         super().display()
# class C(B):
#     def display(self):
#         print('C class')
#         super().display()
# c1=C()
# c1.display()
# print(A.mro())
# print(B.mro())
# print(C.mro())



'''Question-2'''
class CustomIterator:
    def __init__(self,l):
        self.l=l
    def __iter__(self):
        self.i=0
        self.k=0
        return self
    def __next__(self):
        self.i+=1
        # print('vb',self.k)
        if (self.i-1) <len(self.l):
            # print('w')
            if self.l[self.i-1]>self.k:
                # print('q')
                self.k=self.l[self.i-1]
                return self.k
            else:
                # print('p')
                self.k=self.k
                return self.k
        else:
            raise StopIteration
c1=CustomIterator([6,7,5,3,8,1,9])
c2=CustomIterator([0,3,2,7,2])
for i in c1:
    print(i)


# '''Question-3'''
# class CoffeeMachine:
#     def __init__(self,b,ct,p,ca):
#         self.brand=b
#         self.coffee_type=ct
#         self.price=p
#         self.cups_available=ca
#     def  make_coffee(self):
#         self.cups_available-=1
#         print( 'Coffee is Ready')
#     def refill_cups(self,quantity):
#         self.cups_available+=quantity
#         print( f'{self.cups_available} Cups_Available')
#     def display_details(self):
#         print(f' Coffee_Machine_Brand: {self.brand}\n'
#               f'Coffee_Type: {self.coffee_type}\n'
#               f'Price: {self.price}\n'
#               f'Cups_Available: {self.cups_available}')
#     def __str__(self):
#         return (f'Coffee_Machine_Brand is "{self.brand}",\n'
#                 f'"{self.coffee_type}" type Coffee is Extracted,\n'
#                 f'It Costs around INR "{self.price}/-"\n'
#                 f'{self.cups_available} cups available.')
#     def __len__(self):
#         return f'{self.cups_available} Cups of Coffee Available'
#     def __add__(self, other):
#         return f'Total No: {(self.cups_available)+(other.cups_available)} Cups'
# m1=CoffeeMachine('Tata','Cold Coffee',60,10)
# m2=CoffeeMachine('Safari','Black Coffee',90,5)
# print(m1)
# m2.display_details()
# print(m1+m2)


