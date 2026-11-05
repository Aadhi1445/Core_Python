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

# def calculate(x, y):
#     print('Sum:', x + y)
# t1 = threading.Thread(target=calculate, args=(10, 20))
# t1.start()
# t1.join()
# print('Main Thread Completed')


# '''4. Write a Python program where two threads increment a shared variable named
# counter exactly 100000 times each without using any synchronization mechanism,
# and print the final value of the counter to demonstrate inconsistent or
# incorrect results caused by a race condition.'''
# x=0
# def fun():
#     global x
#     for i in range(10000):
#         x+=1
# print(x)
# t1=threading.Thread(target=fun)
# t2=threading.Thread(target=fun)
# t1.start()
# t2.start()
# t1.join()
# t2.join()
# print(x)

# '''5. Modify the previous program so that the shared variable counter is updated
# in a thread-safe manner using threading.Lock, and ensure that the final printed
# value of the counter is always correct.'''
# x=0
# l=threading.Lock()
# # def fun():
# #     global x
# #     with l:
# #         for i in range(10000):
# #             x+=1
# def fun():
#     global x
#     for i in range(10000):
#         with l:
#             x+=1
# print('x:',x)
# t1=threading.Thread(target=fun)
# t2=threading.Thread(target=fun)
# t1.start()
# t1.join()
# t2.start()
# t2.join()
# print(x)

# '''6. Write a Python program where one thread prints “A started” and then sleeps
# for two seconds, another thread prints “B started”, and the execution order is
# controlled in such a way that the second thread starts only after the first
# thread has completely finished.'''
# class A(threading.Thread):
#     def __init__(self,n):
#         super().__init__()
#         self.name=n
#
#     def run(self):
#         print(f'{self.name} Started ')
#         time.sleep(2)
# t1=A('Thread 1')
# t2=A('Thread 2')
# t1.start()
# t1.join()
# t2.start()
# t2.join()
# print('Main Ended')
'''7. Write a Python program in which three worker threads wait until a synchronization signal is received, 
the main thread sleeps for two seconds and then signals all waiting threads using an event, 
after which each worker thread prints a message indicating that it has started execution.'''
'''8. Write a Python program that creates five threads competing for a shared resource, 
restricts access so that only two threads can enter the critical section at the same time using a semaphore,
 and prints a message whenever a thread enters and exits the critical section. 
 9. Write a Python program that starts a daemon thread running an infinite loop which 
 repeatedly prints “Running in background”,  while the main thread sleeps for two seconds and then exits,
and observe what happens to the daemon thread when the main program terminates. 

 10. Write a Python program using ThreadPoolExecutor with three worker threads that submits tasks to compute the 
 square of numbers from 1 to 5 and prints each result as soon as the corresponding task completes.'''

# from concurrent.futures import ThreadPoolExecutor
#
# def task(n):
#     print(f"Task {n} executing")
#     time.sleep(2)
#     return n * 10
#
# with ThreadPoolExecutor(max_workers=2) as executor:
#     f1 = executor.submit(task, 1)
#     f2 = executor.submit(task, 2)
#     # f3 = executor.submit(task, 3)
#     # f4 = executor.submit(task, 4)
#     print('f1: ',f1)
#     print('f2 :',f2)
#     # print('f3 :',f3)
#     # print('f4 :',f4)
#     print(f1.done())
#     print(f2.done())
#     # print(f3.done())
#     # print(f4.done())
#     print(f1.result())
#     print(f2.result())
#     # print(f3.result())
#     # print(f4.result())
#     print(f1.done())
#     print(f2.done())
#     # print(f3.done())
#     # print(f4.done())
#
# print("Main completed")