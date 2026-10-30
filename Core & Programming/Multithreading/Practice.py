import threading
import time
# ''' 1. Write a Python program that creates a worker thread which prints “Hello
# from worker thread” while the main thread prints “Hello from main thread”, and
# ensure that the main thread waits for the worker thread to finish execution
# before the program exits.'''
# def fun():
#     print('Hello from worker thread')
# t1=threading.Thread(target=fun)
# t1.start()
# t1.join()
# print('Hello From main thread')
# '''2. Write a Python program that creates three separate threads where each
# thread prints numbers from 1 to 5, and every printed number must be prefixed
# with the name of the thread that printed it, such as “Thread-1: 3”.'''
# def fun1():
#     for i in range(1,11):
#         print(f'"{threading.current_thread().name}: {i}"')
# def fun2():
#     for i in range(1,11):
#         print(f'"{threading.current_thread().name}: {i}"')
# def fun3():
#     for i in range(1,11):
#         print(f'"{threading.current_thread().name}: {i}"')
# t1=threading.Thread(target=fun1,name='Thread-1')
# t2=threading.Thread(target=fun2,name='Thread-2')
# t3=threading.Thread(target=fun3,name='Thread-3')
# l=[t1,t2,t3]
# for i in l:
#     i.start()
#     # i.join()
# for i in l:
# #     # i.start()
#     i.join()
# print('Main Thread Completed')

# print('-'*9)

# def fun1():
#     for i in range(1,11):
#         print(f'"{threading.current_thread().name}: {i}"')
#         time.sleep(1)
# def fun2():
#     for i in range(1,11):
#         print(f'"{threading.current_thread().name}: {i}"')
#         time.sleep(1)
# def fun3():
#     for i in range(1,11):
#         print(f'"{threading.current_thread().name}: {i}"')
#         time.sleep(1)
# t1=threading.Thread(target=fun1,name='Thread-1')
# t2=threading.Thread(target=fun2,name='Thread-2')
# t3=threading.Thread(target=fun3,name='Thread-3')
# l=[t1,t2,t3]
# for i in l:
#     i.start()
#     # i.join()
# for i in l:
# #     # i.start()
#     i.join()
# print('Main Thread Completed')

'''3. Write a Python program in which a thread accepts two integer arguments,
computes their sum, prints the result from inside the thread, and ensures that
the main thread waits until the worker thread completes execution.'''

# class A(threading.Thread):
#     def __init__(self,x,y):
#         self.x=x
#         self.y=y
#     def run(self):
#         print('sum :',self.x+self.y)
# t1=A(2,3)
# t1.start()
# t1.join()
# print('Main Thread Completed')

def calculate(x, y):
    print('Sum:', x + y)
t1 = threading.Thread(target=calculate, args=(10, 20))
t1.start()
t1.join()
print('Main Thread Completed')


'''4. Write a Python program where two threads increment a shared variable named
counter exactly 100000 times each without using any synchronization mechanism,
and print the final value of the counter to demonstrate inconsistent or
incorrect results caused by a race condition.
5. Modify the previous program so that the shared variable counter is updated
in a thread-safe manner using threading.Lock, and ensure that the final printed
value of the counter is always correct.
6. Write a Python program where one thread prints “A started” and then sleeps
for two seconds, another thread prints “B started”, and the execution order is
controlled in such a way that the second thread starts only after the first
thread has completely finished.'''