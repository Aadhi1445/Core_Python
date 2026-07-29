# def fun
# def electricty(rate_per_unit):
#     def inner(units):
#         total_bill=rate_per_unit*units
#         print(f'Total Bill : {total_bill}')
#     return inner
# e=electricty(5)
# e(150)

# def salary(bonus):
#     def inner(basic_salary):
#         total_salary=bonus+basic_salary
#         print(f'Total salary : {total_salary}')
#     return inner
# s=salary(20000)
# s(40000)

# def dicount(percent):
#     def inner(product_price):
#         total_price=product_price-(percent/100*product_price)
#         print(f'Total price With discount : {total_price}')
#     return inner
# p=dicount(10)
# p(100)

# def bank_account(balance):
#     def inner(withdraw_amount):
#         remaing_amount=balance-withdraw_amount
#         print(f'Amount after Withdraw : {remaing_amount}')
#     return inner
# b=bank_account(50000)
# b()

# def fun(a,b):
#     print(a+b)
# print(a,b)
# fun(10,20)
# # print(a,b)

'''Question 1

Write a function electricity(rate_per_unit).

The outer function receives the cost per unit.
The inner function receives the number of units consumed.
Print the total electricity bill.
Return the inner function.'''
# def electricity(rate_per_unit):
#     def consume(x):
#         print(rate_per_unit*x)
#     return consume
# k=electricity(5)
# k(5)
'''
Question 2
Write a function salary(bonus).
The outer function receives the bonus amount.
The inner function receives the employee's basic salary.
Print the total salary after adding the bonus.
Return the inner function.'''
# def salary(bonus):
#     def basic_salary():
#         k=5000
#         print(k+bonus)
#     return basic_salary
# e1=salary(1000)
# e1()
'''Question 3
Write a function discount(percent).
The outer function receives the discount percentage.
The inner function receives the product price.
Print the final price after applying the discount.
Return the inner function.'''
# def discount(y):
#     def product_price(x):
#         final_price=x+((y/100)*x)
#         print(final_price)
#     return product_price
# k=discount(10)
# k(100)

'''Question 4
Write a function bank_account(balance).
The outer function receives the initial balance.
The inner function receives an amount to withdraw.
Print the remaining balance.
Return the inner function.'''
# def bank_acc(initial_balance):
#     def withdraw(amount):
#         print(initial_balance-amount)
#         return initial_balance-amount
#     return withdraw
# k=bank_acc(10000)
# k(1000)
# # print(k(1000))
'''Question 5
Write a function movie(movie_name).
The outer function stores the movie name.
The inner function receives the person's name.
Print that the person booked a ticket for the movie.
Return the inner function.'''

# def movie_name(movie_name):
#     def person_name(person_name):
#         print(f"{person_name} booked a ticket for '{movie_name}' movie. ")
#     return person_name
# p1=movie_name('Salaar')
# p1('Aadhi')

'''Question 6
Write a function multiplier(number).
The outer function receives one number.
The inner function receives another number.
Print their multiplication.
Return the inner function.'''
# def multiplier(y):
#     def num(x):
#         print(y**x)
#     return num
# k=multiplier(int(input()))
# k(int(input()))
'''Question 7
Write a function restaurant(food_item).
The outer function stores the food item.
The inner function receives the quantity.
Print the order details.
Return the inner function.'''
# def food_item(name):
#     def quantity(quantity):
#         print(name,':',quantity)
#     return quantity
# o1=food_item('fried_rice')
# o1(30)
'''Question 8
Write a function create_password(password).
The outer function stores the original password.
The inner function receives another password.
If both passwords are the same, print Access Granted.
Otherwise, print Access Denied.
Return the inner function.'''
# def password(x):
#     def another_password(y):
#         if x==y:
#             print("Access Granted")
#         else:
#             print("Access Denied")
#     return another_password
# p1=password('Aadhi1445')
# p1('Aadhi1445')
# p2=password('Aadhi1445')
# p1('adhi1445')
'''Question 9
Write a function shopping_cart(item_name).
The outer function receives the item name.
The inner function receives:
quantity,price_per_item
Print the item name, quantity, and total price.
Return the inner function.'''
# def shopping_cart(item_name):
#     def inner(quantity,price_per_item):
#         total_price=quantity*price_per_item
#         print('item name:',item_name)
#         print('quantity:',quantity)
#         print("total price:",total_price)
#     return inner
# s1=shopping_cart("laptop")
# s1(3,20000)
'''Question 10
Create a function counter().
Inside it, initialize a variable count = 0.
Create an inner function that increments count by 1 every time it is called.
Print the updated value of count.
Return the inner function.
Call the returned function five times.'''
# def counter():
#     c=0
#     def inner():
#         nonlocal c
#         c+=1
#         print(c)
#         return c
#     return inner
# d=counter()
# print(d())
# print(d())
# print(d())
# print(d())
# d()
