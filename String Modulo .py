String Modulo 
You are given 2 numbers N & P. Print N % P.



Input Format

The first line of input contains T - the number of test cases. It's followed by T lines, each line contains 2 numbers N and P, separated by space.



Output Format

For each test case, print the value of N % P, separated by a new line.



Constraints

20 points

1 <= T <= 100

1 <= N <= 1018

1 <= P <= 108



80 points

1 <= T <= 100

1 <= N <= 1010000

1 <= P <= 1015



Example

Input

4

5 2

4 10

1085377843 81765943

8290826691135830692772803 95972011



Output

1

4

22420584

60316167



Explanation



Self Explanatory




# Enter your code here. Read input from 
for _ in range(int(input())):
    a,b=map(str,input().split())
    res=0
    for i in range(len(a)):
        res=(res*10+int(a[i]))%int(b)
    print(res)