import time
# ''' Without Multithreading'''
# def fun1():
#     for i in range(1,4):
#         print('fun 1:',i)
#         time.sleep(1) # here fun1 waits 1sec after printing every i value
# def fun2():
#     for i in range(1,4):
#         print('fun 2:',i)
#         time.sleep(2) # here fun1 waits 2sec after printing every i value
# fun1()
# fun2()
import  threading
''' With Multithreading'''
# def fun1():
#     for i in range(3):
#         print('fun1: ',i)
#         time.sleep(1)
#
# def fun2():
#     for i in range(3):
#         print('fun2: ',i)
#         time.sleep(2)
#
# t1=threading.Thread(target=fun1)
# t2=threading.Thread(target=fun2)
#
# t1.start()
# t2.start()


# JOIN -->  join joins the threads to main thread
''' with Join '''
# def fun1():
#     for i in range(3):
#         print('fun1: ',i)
#         time.sleep(1)
#
# def fun2():
#     for i in range(3):
#         print('fun2: ',i)
#         time.sleep(2)
#
# t1=threading.Thread(target=fun1)
# t2=threading.Thread(target=fun2)
#
# t1.start()
# t2.start()
#
# t1.join()
# t2.join()
# print('Both threads Executed')

''' without Join '''

# def fun1():
#     for i in range(3):
#         print('fun1: ',i)
#         time.sleep(1)
#
# def fun2():
#     for i in range(3):
#         print('fun2: ',i)
#         time.sleep(2)
#
# t1=threading.Thread(target=fun1)
# t2=threading.Thread(target=fun2)
#
# t1.start()
# t2.start()
#
# print('Both threads Executed')

''' with 3 threads'''

# import threading
# import time
#
# def task1():
#     for i in range(1, 4):
#         print("Task 1:", i)
#         time.sleep(1)
#
# def task2():
#     for i in range(1, 4):
#         print("Task 2:", i)
#         time.sleep(1)
#
# def task3():
#     for i in range(1, 4):
#         print("Task 3:", i)
#         time.sleep(1)
#
#
# t1 = threading.Thread(target=task1, name="Thread-1")
# t2 = threading.Thread(target=task2, name="Thread-2")
# t3 = threading.Thread(target=task3, name="Thread-3")
#
# t1.start()
# t2.start()
# t3.start()
#
# t1.join()
# t2.join()
# t3.join()
#
# print("All three tasks completed")


''' Name Parameter in thread constructor'''
#is_alive()--Checks whether a thread has started and has not yet finished.
def task():
    print("Hello from a thread")
    print("Running thread:", threading.current_thread().name)

t1 = threading.Thread(target=task, name="MyWorker")

t1.start()
print(t1.is_alive())
t1.join()
