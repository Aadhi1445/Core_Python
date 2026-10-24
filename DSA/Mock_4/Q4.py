'''
Write a Program to Print the Right Angle Triangle Program with Prime Numbers and Fibonacci Numbers Alternatively?


Input :             First Line of the Input Consists of One Integer Value

Output :          Print the Pattern as Shown in the Pattern.
Constraints
Given Number Must be Greater Than Zero or else Print "Invalid Input".
Public examples
Sample 1
Input

5
Output

2
0 3
1 5 1
7 2 11 3
13 5 17 8 19
Sample 2
Input

8
Output

2
0 3
1 5 1
7 2 11 3
13 5 17 8 19
13 23 21 29 34 31
55 37 89 41 144 43 233
47 377 53 610 59 987 61 1597
Sample 3
Input

0
Output

Invalid Input

'''

n=int(input())
if n<=0:
    print("Invalid Input")
else:
    a,b=0,1
    ct=0
    g=True
    p=2
    for i in range(n):
        for j in range(i+1):
            ct+=1
            if ct%2==1:
                g=True
                while g:
                    for j in range(2,p):
                        if p%j==0:
                            break
                    else:
                        print(p,end=" ")
                        g=False
                    p+=1
            else:
                g=True
                while g:
                    g=False
                    print(a,end=" ")
                    c=a+b
                    a=b
                    b=c
        print()