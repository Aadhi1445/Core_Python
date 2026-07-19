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
class Course:
    total_courses=0
























