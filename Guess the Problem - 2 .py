Guess the Problem - 2 
Understand the problem statement from the given sample input and output.



Input Format

The first line of input contains T - the number of test cases. It's followed by T lines, each line contains a string consisting only of lowercase English alphabets and an integer K.



Output Format

For each test case, print the desired output, separated by a new line.



Constraints

1 <= T <= 1000

1 <= len(str) <= 1000

0 <= k <= 100000



Example

Input

2

smart 3

interviews 10



Output

vpduw

sxdobfsogc



Explanation



Self Explanatory



# Enter your code here. Read input from ST
t=int(input())
while t>0:
    a,b=list(map(str,input().split()))
    k=int(b)
    for i in range(len(a)):
        q=ord(a[i])
        w=q-97
        e=w+k
        r=e%26
        print(chr(r+97),end="")
    print()
    t-=1