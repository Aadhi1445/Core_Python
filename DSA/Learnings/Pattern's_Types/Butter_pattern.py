'''Write a program to print the following pattern
*                     *
* *                * *
* * *           * * *
* * * *      * * * *
* * * * * * * * * *
* * * *      * * * *
* * *           * * *
* *                * *
*                     *
Constraints
Input :                   First line of input consists of one integer value.
Output :                Print the given pattern
Constraints :         NA
Example
Input :          4
Output :
*                *
* *           * *
* * *      * * *
* * * * * * * *
* * *      * * *
* *           * *
*                *'''
n=int(input())
for i in range(1,n+1):
    print("* "*i,end="")
    print("    "*(n-i),end="")
    print("* "*(i),end="")
    print()
for i in range(n-1,0,-1):
    print("* "*(i),end="")
    print("    "*(n-i),end="")
    print("* "*(i),end="")
    print()