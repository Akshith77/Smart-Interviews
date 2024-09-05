Finding CubeRoot 
Find the cube root of the given number. Assume that all the input test cases will be a perfect cube.



Note: Do not use any inbuilt functions / libraries for your main logic.

Input Format

The first line of input contains T - the number of test cases. It is followed by T lines, each containing a single integer.



Output Format

For each test case, print the cube root of the number, separated by a new line.



Constraints

30 points

1 <= T <= 103

-109 <= N <= 109



70 points

1 <= T <= 106

-1018 <= N <= 1018



Example

Input

5

-27

-125

1000

6859

-19683



Output

-3

-5

10

19

-27



Explanation



Self Explanatory


# Enter your code here. Read input from STDIN. Print outpu
def cube(n,f):
    l,h=0,n
    m=0
    while l<=h:
        m=(l+h)//2
        t=m*m*m
        if t==n:
            return m
        elif t>n:
            h=m-1
        else:
            l=m+1

for _ in range(int(input())):
    n=int(input())
    f=1
    if n<0:
        f=-1
    print(f*cube(abs(n),f))