import time
import threading

# class A(threading.Thread):
#     def run(self):
#         print('A Class custom thread')
# t1=A()
# t2=A()
# t1.start()
# t2.start()

''' ------ '''

# class MyThread(threading.Thread):
#
#     def __init__(self, task_name):
#         super().__init__()
#         self.task_name = task_name
#
#     def run(self):
#         print(self.task_name, "is running")
#
#
# t1 = MyThread("Python")
# t2 = MyThread("SQL")
# t3 = MyThread("Django")
#
# t1.start()
# t2.start()
# t3.start()

# t1.join()
# t2.join()
# t3.join()
# print("All custom threads completed")


# def display(subject):
#     for i in range(1, 4):
#         print(subject, i)
#
# t1 = threading.Thread(target=display, args=("Python",))
# t2 = threading.Thread(target=display, args=("SQL",))
# t3 = threading.Thread(target=display, args=("Django",))
#
# t1.start()
# t2.start()
# t3.start()
#
# t1.join()
# t2.join()
# t3.join()
#
# print("Completed")



''' Without Lock'''

# import threading
#
# balance = 1000
#
# def withdraw():
#     global balance
#
#     if balance >= 800:
#         balance -= 800
#         print("Withdrawal successful:", balance)
#     else:
#         print("Insufficient balance:", balance)
#
# t1 = threading.Thread(target=withdraw)
# t2 = threading.Thread(target=withdraw)
#
# t1.start()
# t2.start()
#
# t1.join()
# t2.join()
#
# print("Final balance:", balance)


''' with lock'''
# import threading
#
# lock = threading.Lock()
#
# def task(name):
#     with lock:
#         print(name, "entered")
#         print(name, "is working")
#         print(name, "exited")
#
# t1 = threading.Thread(target=task, args=("Thread A",))
# t2 = threading.Thread(target=task, args=("Thread B",))
#
# t1.start()
# t2.start()
#
# t1.join()
# t2.join()


# import threading
#
# class BankAccount:
#     def __init__(self, balance):
#         self.balance = balance
#         self.lock = threading.Lock()
#
#     def withdraw(self, amount):
#         with self.lock:
#             if self.balance >= amount:
#                 self.balance -= amount
#                 print(f"Withdrawn: {amount}")
#                 print(f"Remaining balance: {self.balance}")
#             else:
#                 print("Insufficient balance")
#
#
# account = BankAccount(1000)
#
# t1 = threading.Thread(target=account.withdraw, args=(800,))
# t2 = threading.Thread(target=account.withdraw, args=(800,))
#
# t1.start()
# t2.start()
#
# t1.join()
# t2.join()
#
# print("Final balance:", account.balance)

# import threading
#
# class BankAccount:
#     def __init__(self, balance):
#         self.balance = balance
#         self.lock = threading.Lock()
#
#     def withdraw(self, amount):
#         self.lock.acquire()
#
#         try:
#             if self.balance >= amount:
#                 self.balance -= amount
#                 print("Withdrawn:", amount)
#                 print("Balance:", self.balance)
#             else:
#                 print("Insufficient balance:", self.balance)
#
#         finally:
#             self.lock.release()
#
#
# account = BankAccount(1000)
#
# t1 = threading.Thread(target=account.withdraw, args=(800,))
# t2 = threading.Thread(target=account.withdraw, args=(800,))
#
# t1.start()
# t2.start()
#
# t1.join()
# t2.join()
#
# print("Final balance:", account.balance)


import threading
import time

semaphore = threading.Semaphore(2)
# satwik=threading.lock()
def task(name):
    with semaphore:
        print(name, "entered")
        print("Running thread:", threading.current_thread().name)
        time.sleep(6)
        print(name, "expired")

threads = []

for i in range(1, 5):
    t = threading.Thread(target=task, args=(f"Thread-{i}"))
    threads.append(t)
    t.start()
    t1=threading.thread(target,args,kwargs,name)

for t in threads:
    t.join()

print("All threads completed")