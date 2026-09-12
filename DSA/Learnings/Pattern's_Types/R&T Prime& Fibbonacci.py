'''Write a Program to Print the Right Angle Triangle Program with Prime Numbers and Fibonacci Numbers Alternatively?
Constraints
Input :             First Line of the Input Consists of One Integer Value
Output :          Print the Pattern as Shown in the Pattern.
Constraints :   Given Number Must be Greater Than Zero or else Print "Invalid Input".
Example
Input1 :              5
Output1 :
2
0 3
1 5 1
7 2 11 3
13 5 17 8 19
Input2 :              8
Output2 :
2
0 3
1 5 1
7 2 11 3
13 5 17 8 19
13 23 21 29 34 31
55 37 89 41 144 43 233
47 377 53 610 59 987 61 1597'''
n = int(input())
a, b = 0, 1
p = 2
c = 0
d = 0
if n <= 0:
    print('Invalid Input')
else:
    for i in range(n):
        for j in range(i + 1):
            c += 1
            if c % 2 == 1:
                g = True
                while g:
                    for k in range(2, p):
                        if p % k == 0:
                            break
                    else:
                        print(p, end=" ")
                        g = False
                    p += 1
            else:
                g = True
                while g:
                    g = False
                    print(a, end=' ')
                    # g=False
                    # print(a)
                    d = a + b
                    a = b
                    b = d

        print()