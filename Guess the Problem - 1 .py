Guess the Problem - 1 
Understand the problem statement from the given sample input and output.



Input Format

The first line of input contains T - the number of test cases. It's followed by T lines, each line contains 2 strings A and B, separated by space, consisting only of lowercase English alphabets.



Output Format

For each test case, print the desired output, separated by a new line.



Constraints

10 points

1 <= T <= 100

1 <= len(A), len(B) <= 100



40 points

1 <= T <= 1000

1 <= len(A) <= 5000

1 <= len(A), len(B) <= 5000



Example

Input

2

data structures

smart interviews



Output

srucures

ineview



Explanation



Self Explanatory


# Enter your code here. Read input from STDIN. Print output t
t=int(input())
while t>0:
    a,b=list(map(str,input().split()))
    d={}
    for i in range(len(a)):
        if a[i] in d:
            d[a[i]]+=1
        else:
            d[a[i]]=1
    for j in range(len(b)):
        if b[j] not in d:
            print(b[j],end="")
    print()
    t-=1