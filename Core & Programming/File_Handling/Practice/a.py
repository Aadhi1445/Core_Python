# '''
# • Write a Python program using a context manager (with) to open a text file in read mode,
#     read the entire content using read(), and print the number of characters in the file. '''

# with open('data.txt','r') as file:
    # print(file.tell())
    # k=file.read()
    # print(file.tell())
    # print(len(k))
    # print(k)
    # k=file.readline()
    # print(k)
    # print('k:',k)
    # print('tell:',file.tell()) # here file name should be used
    # print(len(k))
#
#     # k=file.readlines()
#     # for i in k:
#     #     print(i)
#
#     # k = file.readlines()
#     # for i in k:
#     #     print(i,end="")
#
#     # k = file.readlines()
#     # for i in k:
#     #     print(i.strip())
#
#     pass


# ''''• Write a program that opens a file using a context manager, reads all lines using readlines(),
# and prints only the lines that contain more than 10 characters. '''
# with open('data.txt','r') as file:
#     k=file.readlines()
#     for i in k:
#         if len(i)>10:
#             print(i,end="")

# '''• Write a program that creates a file and writes 3 lines using write(),
#     reopens the same file in append mode, appends 2 more lines, and finally reads and prints the complete file content. '''
# with open('data1.txt','w') as file:
#     file.write('abcde\n')
#     file.write('fghij\n')
#     file.write('klmno\n')
# with open('data1.txt','a')as file:
#     file.write('pqrst\n')
#     file.write('uvwxyz\n')
# for i in open('data1.txt').readlines():
#     print(i,end="")
    # file.close()
    # with open ('data1.txt','r') as file1:
    #     k=file1.readlines()
    #     for i in k:
    #         print(i,end="")

# ''''• Write a program that opens a file in read mode, reads the first 10 characters,
#     prints the current cursor position using tell(), moves the cursor back to the beginning using seek(0),
#         and reads the full content again. '''
# with open('data1.txt','r') as file:
#     k=file.read(10)
#     print(k)
#     print(file.tell())
#     file.seek(0)
#     print(file.tell())
#     for i in file.readlines():
#         print(i,end="")


'''• Create a custom context manager using a class that opens a file in write mode in the __enter__ method,
    writes a line to the file, closes the file in the __exit__ method, and
        properly prints or logs any exception information received in __exit__. '''
class A:
    def __init__(self,file,mode):
        self.file=file
        self.mode=mode
    def __enter__(self):
        print('Entered')
        self.k=open(self.file,self.mode)
        return  self.k
    def __exit__(self, exc_type, exc_val, exc_tb):
        # print(2)
        print('\nClosed')
        print('exc_type: ',exc_type)
        print('exc_val :',exc_val)
        print('exc_tb :',exc_tb)
        # return  True
        return self.k.close()
a=A('data1.txt','r')
try:
    with a as f:
        for i in f.readlines():
            print(i,end="")
            # print(1)
            # raise ValueError('Value Error')
except Exception as e:
    # print(3)
    print('e:',e)
    # print(4)

# '''• Create a custom context manager using @contextmanager from the contextlib module that opens a file,
# yields the file object, and ensures the file is closed even if an exception occurs.'''
# # from contextlib import contextmanager
# # @contextmanager
# # def fun(fn,m):
# #     file=open(fn,m)
# #     try:
# #         yield  file
# #     finally:
# #         file.close()
# # with fun('data1.txt','r') as file:
# from contextlib import contextmanager
# @contextmanager
# def manage_file(filename, mode):
#     print("Opening file")
#     f = open(filename, mode)
#     try:
#         yield f
#         # print(2)
#     finally:
#         f.close()
#         print("Closing file")
# with manage_file("data.txt", "w") as f:
#     # print(1)
#     f.write("Hello Python")
# ''''• Write a program using a context manager that opens a file in read mode, uses a loop to read the file in small chunks
#     (for example, 5 characters at a time), prints the cursor position after each read using tell(), uses seek() to move to a specific position,
#         and continues reading from there.'''
# from contextlib import  contextmanager
# # @contextmanager
# with open('data1.txt','r') as f:
#     while True:
#         chunk=f.read(5)
#         if  not chunk:
#             break
#         print(chunk)
#         print(f.tell())
#         # f.seek(6)







