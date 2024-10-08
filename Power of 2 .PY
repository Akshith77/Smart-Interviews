Power of 2 
Given a number, check if it is a power of 2.



Input Format

The first line of input contains T - the number of test cases. It's followed by T lines, each line containing a single positive integer.



Output Format

For each test case, print "True" or "False", separated by a new line.



Constraints

1 <= T <= 10000

1 <= N <= 1018



Example

Input

5

1

8

10

25

512



Output

True

True

False

False

True



Explanation



Self Explanatory

# Enter your code here. Read input from STDIN. Print output to STDOUT
a=int(input())
while a>0:
    b=int(input())
    for i in range(0,b):
        c=pow(2,i)
        if b==c:
            print("True")
            break
        if b<c:
            print("False")
            break
    a-=1