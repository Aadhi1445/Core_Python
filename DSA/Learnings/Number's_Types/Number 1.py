'''Write a program to print the number which is maximum and less than given number and such that the number
must contain given digit and it must greater than zero Constraints
Input :                First line of input consists of an integer
                           Second line of input consists of an integer
Ouput :              print the Number which is greater than zero
Constraints :     No
Example
Input 1 :       126
                      2
Output 1 :    125
Input 2 :        711
                       3
Output 2 :     703
Explanation
Input 1 :     153
                    6
Output 1 :   146
Explanation : Given number is 153 and digit is 6
      Now the maximum number which is less than 153 and contains 6 is 146
Input 2 :        711
                       3
Output 2 :     703
Explanation : Given number is 711 and digit is 3
      Now the maximum number which is less than 711 and contains 3 is 703'''
n=int(input())
k=n
m=int(input())
while n>0 and m>=0:
    r=n%10
    if r==m:
        k=k-1
        break
    n=0
n=k
while n>=0 and m>=0:
    r=n%10
    if r==m and n>0:
        print(n)
        break
    n=n-1