Count Set Bits 
Given a number N, find the number of bits that are set to 1 in its binary representation.



Input Format

The first line of input contains T - the number of test cases. It is followed by T lines, each line contains a single integer N.



Output Format

For each test case, print the number of bits set to 1 in the binary representation of N, separated by a new line.



Constraints

1 <= T <= 104

0 <= N <= 1018



Example

Input

3

4

15

10



Output

1

4

2



Explanation



Test-Case 1

The binary representation of 4 is 100.

The number of 1's in the binary representation of 4 is 1.



Test-Case 2

The binary representation of 15 is 1111.

The number of 1's in the binary representation of 15 is 4.

# Enter your code here. Read input from STDIN. Print output to STDOUT
a=int(input())
while a>0:
    b=int(input())
    c=bin(b)
    d=c[2:]
    q=0
    for i in range(0,len(d)):
        if d[i]=='1':
            q+=1
    print(q)
    a-=1