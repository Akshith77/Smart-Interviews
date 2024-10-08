Flip Bits 
You are given two numbers A and B. Write a program to count the number of bits to be flipped to change the number A to the number B. Flipping a bit of a number means changing a bit from 1 to 0 or vice versa.



Input Format

The first line of input contains T - the number of test cases. Each of the next T lines contains 2 integers A and B, separated by space.



Output Format

For each test case, print the number of bit flips required to convert A to B, separated by a new line.



Constraints

1 <= T <= 100000

0 <= A, B <= 109



Example

Input

4

20 10

16 8

1 153

549 24



Output

4

2

3

6



Explanation



Self Explanatory

def count(n):
    c=0
    while n:
        c+=n&1
        n>>=1
    return c
q=int(input())
while q>0:
    a,b=map(int,input().split())
    print(count(a^b))
    q-=1