# pdf-1 , Q1
# class Student:
#     def __init__(self,name,marks):
#         self.name=name
#         self.marks=marks
#     def is_passed(self):
#         if self.marks>40:
#             return "Passed"
#         else:
#             return "Failed"
#         # return self.marks>40
# s1=Student("parul",55)
# print(s1.is_passed())
# s2=Student("paaru",40)
# print(s2.is_passed())

"""Q1. Create a class Student that:
•	Keeps track of the total number of students created.
•	Determines whether a student passed or failed based on a shared passing mark.
•	Provides a method to curve marks by increasing everyone’s marks by a percentage.
•	Has a utility to convert marks (0–100) into letter grades (A, B, C, etc.).
Demonstrate:
1.	Creating multiple students.
2.	Applying a grading curve.
3.	Displaying updated results with letter grades.
"""
# class Student:
#     total_student=0
#     passing_marks=25
#     l=[]
#     def __init__(self,name,marks):
#         self.name=name
#         self.marks=marks
#         Student.total_student+=1
#         Student.l.append(self)
#     def result(self):
#         if self.marks>=Student.passing_marks:
#             return "passed"
#         else:
#             return "failed"
#     def grades(self):
#         if self.marks>=85:
#             return "A"
#         elif self.marks>=70:
#             return "B"
#         elif self.marks>=55:
#             return "C"
#         elif self.marks>=40:
#             return "D"
#         elif self.marks>=25:
#             return "E"
#         else:
#             return "F"
#     def display(self):
#         print(self.name,self.marks,self.result(),self.grades(),Student.total_student)
#     @staticmethod
#     def curve_marks(marks,):
#         marks=marks+()
# s1=Student("John",34)
# # s1.display()
# s2=Student("Michael",35)
# # s2.display()
# # print(Student.l)
"""Q2. Design a class Product that:
•	Maintains a base tax rate applicable to all products.
•	Each product has a name and base price.
•	Has a method to compute final price including tax.
•	Can change tax rate for all products using one method.
•	Includes a function to check whether a given price is valid or not (non-negative and realistic).
Demonstrate:
1.	Creating multiple products.
2.	Changing the tax rate.
3.	Showing updated prices and validity checks.
"""
# class Product:
#     base_tax=10
#     def __init__(self,name,base_price):
#         self.name=name
#         self.base_price=base_price
#     def final_price(self):
#         final_price=self.base_price+((Product.base_tax/100)*self.base_price)
#         return final_price
#     @classmethod
#     def n_tax_rate(cls,n_tax):
#         Product.base_tax=n_tax
#         # cls.base_tax = n_tax
#         return Product.base_tax
#     def check(self):
#         if self.base_price>0:
#             return "Valid"
#         else:
#             return "Invalid"
# a=Product("box",25)
# b=Product("pen",0)
# c=Product("glass",20)
# # print(a.final_price())
# # print(b.final_price())
# print(c.final_price())
# Product.n_tax_rate(20)
# # print(a.final_price())
# # print(b.final_price())
# print(c.final_price())
# # print(a.check())
# # print(b.check())
# print(c.check())

"""Q3. Create an Employee class that:
•	Keeps a minimum experience required for promotion (shared across all employees).
•	Stores employee name, experience, and department.
•	Has a method to check eligibility for promotion.
•	Provides a function to update promotion criteria globally.
•	Offers a general tool that checks if a given department is valid (like “HR”, “Tech”, “Admin”).
Demonstrate:
1.	Creating employees from different departments.
2.	Changing promotion criteria.
3.	Displaying eligibility results and department validation.
"""
# class Employee:
#     min_exp=4
#     valid_dept=["Hr",'Tech','Admin']
#     def __init__(self,name,exp,dept):
#         self.name=name
#         self.exp=exp
#         self.dept=dept
#     def eligibility(self):
#         if self.exp>=Employee.min_exp:
#             return "Eligible"
#         else:
#             return "Not Eligible"
#     @classmethod
#     def chang_promotion(cls,n_exp):
#         Employee.min_exp=n_exp
#     @staticmethod
#     def check(dept):
#         if dept in Employee.valid_dept:
#             return dept
#         else:
#             return "Invalid Department"
# e1=Employee("Aadhya",6,"Tech")
# e2=Employee("kesava",3,"Admin")
# e3=Employee("mani",4,"ap")
# # # # print(Employee.check(e1.dept))
# # # # print(Employee.check(e3.dept))
# # # print(e1.eligibility())
# # # print(e2.eligibility())
# # Employee.chang_promotion(5)
# # print(Employee.min_exp)
# # print(e1.eligibility())
# # print(e2.eligibility())
"""Q4. Build a Loan class that:
•	Has a common interest rate for all loans.
•	Each object stores borrower name and principal.
•	Calculates total payable amount.
•	Provides a function to update the interest rate.
•	Provides a static function to check loan eligibility (e.g., salary > certain threshold).
Demonstrate:
1.	Creating multiple loan accounts.
2.	Updating interest rates.
3.	Checking eligibility and total repayment for borrowers.
"""
# class Loan:
#     interest_rate=5
#     threshold=1500
#     def __init__(self,name,principal,salary,years=1):
#         self.name=name
#         self.principal=principal
#         self.salary=salary
#         self.years=years
#     def total_payable(self):
#         total_payable=self.principal+self.years*((Loan.interest_rate/100)*self.principal)
#         return total_payable
#     @classmethod
#     def update_interest(cls,n_interest):
#         Loan.interest_rate=n_interest
#         return Loan.interest_rate
#     @staticmethod
#     def eligibility(salary):
#         if salary>Loan.threshold:
#             return "Eligible"
#         else:
#             return "Not Eligible"
# b1=Loan("Parul",5000,1800,2)
# print(Loan.eligibility(b1.salary))
# print(b1.total_payable())
# Loan.update_interest(4)
# print(Loan.interest_rate)
# b1=Loan("Parul",5000,1800,2)
# print(Loan.eligibility(b1.salary))
# print(b1.total_payable())
# Loan.update_interest(0)
# print(Loan.interest_rate)
# print(b1.total_payable())
# b2=Loan("satwik",10000,2000,4)
# print(b2.total_payable())
# print(Loan.eligibility(b2.salary))
"""Q5. Create a class Course that:
•	Tracks total courses created.
•	Each course has a title, duration, and enrolled_students.
•	Provides a method to enroll a new student.
•	Allows updating the minimum duration for a valid course across all instances.
•	Has a static function to check if a given duration is realistic (not negative, not too large).
Demonstrate:
1.	Creating multiple courses.
2.	Enrolling students.
3.	Updating minimum duration and checking durations
"""
# class Course:
#     total_courses=0
#     min_duration=20
#     def __init__(self,title,dur,e_stu):
#         self.title=title
#         self.duration=dur
#         self.e_students=e_stu
#         Course.total_courses+=1
#     def enroll(self,n):
#         self.e_students+=n
#         return self.e_students
#     @classmethod
#     def update(cls,x):
#         cls.min_duration=x
#     @staticmethod
#     def valid_dur(dur):
#         if dur>0 and dur >= Course.min_duration:
#             return dur
# # print(Course.valid_dur(15))
# c1=Course("Python",30,55)
# c2=Course("Java",25,50)
# c1.enroll(5)
# print(c1.e_students)

"""Q6. Design a class Vehicle that:
•	Keeps a record of service charge rate common to all vehicles.
•	Each vehicle has a model, kilometers_run, and service history.
•	Has a function to calculate service charge based on km and rate.
•	Provides a method to update the service rate for all vehicles.
•	Provides a static tool to check if a vehicle model is eligible for service (not older than 15 years).
Demonstrate:
1.	Creating vehicles with different km and models.
2.	Updating the service rate.
3.	Showing charges and eligibility checks."""
# class Vehicle:
#     s_charge=100
#     def __init__(self, model, km_r, history=0):

#         self.model=model
#         self.km_r=km_r
#         self.history=history
#     @staticmethod
#     def cal(x):
#         print(Vehicle.s_charge*x+Vehicle.s_charge)
#     @classmethod
#     def update(cls,z):
#         cls.s_charge=z
#         return cls.s_charge
#     @staticmethod
#     def eligible(a):
#         if a<=15:
#             print("Eligible")
#         else:
#             print("Not Eligible")
#         return a
# v1=Vehicle("hero",5000,2)
# v2=Vehicle("glamour",2500)
# Vehicle.eligible(5)
# Vehicle.cal(200)
# Vehicle.update(200)
# Vehicle.cal(200)

"""Q7. Build an Inventory class that:
•	Tracks the total number of items across all inventories.
•	Each instance maintains its own stock dictionary ({"item": quantity}).
•	Provides a method to add or remove stock.
•	Allows updating a minimum stock threshold globally.
•	Offers a static checker to verify if a stock level is below threshold.
Demonstrate:
1.	Managing multiple inventories.
2.	Adjusting stock threshold.
3.	Using static validation inside the instance logic."""
# class Inventory:
#     total_items=0;thresshold=20
#     def __init__(self):
#         self.stores={}
#     def add(self,item,qty):
#         if self.valid(qty):
#             self.stores[item]=qty
#             Inventory.total_items+=1
#             print("Item Added Succefully")
#         else:
#             print("Quantity should Reach Min thresshold")
#     @staticmethod
#     def valid(qty):
#         return qty>Inventory.thresshold
#     def remove(self,item):
#         if item in self.stores.keys():
#             self.stores.pop(item)
#             Inventory.total_items-=1
#             print("item succesfully removed from inventory")
#         else:
#             print("item not found")
# v1=Inventory()
# v1.add("pen",56)

"""Q8. Create a HotelRoom class that:
•	Keeps a base price per night (shared).
•	Each room has room_number, nights_booked, and guest_name.
•	Has a method to calculate total bill.
•	Allows updating the base price across all rooms.
•	Provides a static utility to check if a number of nights is valid (e.g., positive integer only).
Demonstrate:
1.	Creating rooms and bookings.
2.	Changing base price.
3.	Checking bill updates and validation"""
# class Hotel:
#     b_price=250
#     def __init__(self,r_num,nyt_booked,g_name):
#         self.r_num=r_num
#         self.nyt_booked=nyt_booked
#         self.g_name=g_name
#     @classmethod
#     def update(cls,x):
#         Hotel.b_price=x
#         return Hotel.b_price
#     @staticmethod
#     def check(y):
#         if y>0:
#             print("Valid")
#         else:
#             print("Invalid")
#         return y
#     def cal(self):
#         return self.nyt_booked*Hotel.b_price
# g1=Hotel(5,4,"Aadhya")
# print(Hotel.cal(g1))
# print(g1.cal())

"""Q9. Design a LibraryMember class that:
•	Tracks total active members.
•	Each member has a name and books_borrowed count.
•	Has a function to borrow books, with borrowing limit common to all.
•	Allows updating borrowing limit globally.
•	Has a static function to check if book title is valid (non-empty string, reasonable length).
Demonstrate:
1.	Borrowing books for multiple users.
2.	Changing borrowing limits.
3.	Validating book titles before borrowing."""
 # class LibraryMem:
 #     total_a_mem=0
 #     b_limit=10
 #     def __init__(self,name,books_borrowed_count):
 #         self.name=name
 #         self.books_borrowed_count=books_borrowed_count
 #         LibraryMem.total_a_mem+=1
 #     @staticmethod
 #     def check(title):
 #         return len(title)<30
 #     @classmethod
 #     def update(cls,n):
 #         LibraryMem.b_limit=n
 #     def borrow(self):
 #         if

'''Q10. Create a class Member that:
•	Has a shared BMI limit for “fit” status.
•	Each member stores name, height, weight.
•	Has a method to calculate BMI and check fit status.
•	Provides a function to update BMI limit for all members.
•	Offers a tool to check if height and weight entered are valid numbers.
Demonstrate:
1.	Creating multiple members.
2.	Updating BMI standard.
3.	Displaying fit status and input validity.'''
# class Member:
#     bmi_limit= 25
#     def __init__(self,name,height,weight):
#         self.name=name
#         self.height=round(height,1)
#         print(self.height)
#         self.weight=weight
#     def cal_bmi(self):
#         k=self.weight//(self.height**2)
#         # k=round(k,1)
#         if 18 < k < 25:
#             print(k,"fit")
#         else:
#             print(k,"Unfit")
#         return k
#     @staticmethod
#     def check_bmi(a):
#         if a>=25:
#             print("Unfit")
#         elif 18<=a<=25:
#             print("fit")
#         else:
#             print("Unfit")
#         return a
#     @staticmethod
#     def valid(height,weight):
#         if height>0 and weight>0:
#             print("valid height & weight")
#         elif height<=0:
#             print("Invalid Height")
#         elif weight <=0:
#             print("Invalid Weight")
#         else:
#             print("Invalid Height & weight")
#         return height,weight
# # u1=Member(input("Enter name"),int(input("enter Height")),int(input("enter weight")))
# u1=Member("aadhya",2.657,50)
# u1.cal_bmi()


    












































