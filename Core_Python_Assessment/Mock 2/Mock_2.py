# # '''Question-1'''
# class Book:
#     total_books=0
#     def __init__(self,title,author):
#         if Book.is_valid(title):
#             self.title=title
#         else:
#             print("Invalid title")
#         self.author=author
#         Book.total_books+=1
#     @staticmethod
#     def is_valid(title):
#         return len(title)>=3
#     @classmethod
#     def validating_title(cls,book_str):
#         title,author=book_str.split("-")
#         return cls(title,author)
# b1=Book.validating_title("science-tagore")
# b2=Book.validating_title("social-govind")
# print("ttile:",b2.title)
# print("Author:",b2.author)
# b3=Book("Aadhya","driving")
# print("ttile:",b3.title)
# print("Author:",b3.author)


# '''Question-3'''
def create_password(password):
    def inner_password(a_password):
        if password==a_password:
            print("Access Granted")
        else:
            print("Access Denied")
    return inner_password
p1=create_password("Aadhya123")
p1("Aadhya123")
p2=create_password("shyam")
p2("aditya")

# '''Question-2'''
class Water_tank:
    def __init__(self,name,water_lever=0):
        self.name=name
        self.water_level=water_lever
    def __str__(self):
        return f'"{self.name}" has {self.water_level}Units water level.\n'
    def __repr__(self):
        return f'Name="{self.name}"\nWater_lavel={self.water_level}\n'
    def __add__(self,z):
        self.water_level+=z
        return f'Existing Water level :{self.water_level}'
    def __truediv__(self,z):
        k=self.water_level+z.water_level
        self.water_level=k/2
        z.water_level=k/2
        return f'Existing Water level:{self.water_level}\nExisting Water level:{z.water_level}5\n'
    def __sub__(self,z ):
        self.water_level-=z
        return f'Existing Water level :{self.water_level}'
t1=Water_tank("Sadhya",300)
print(t1)
print(t1+200)
print(t1-200)
print(repr(t1))
t2=Water_tank("Rocky",150)
print(t2)
print(t2+200)
print(t2-200)
print(repr(t2))
print(t1/t2)
print(t1)
print(t2)
