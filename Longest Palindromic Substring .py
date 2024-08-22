Longest Palindromic Substring 
Given a string, find the length of the Longest Palindromic Substring (LPS).



Input Format

The first line of input contains T - the number of test cases. It's followed by 2T lines. The first line has N - the size of the string and the second line contains a string of size N.



Output Format

Print the length of the LPS for each test case, separated by a new line.



Constraints

30 points

1 <= T <= 200

1 <= len(S) <= 100

'a' <= S[i] <= 'z'



70 points

1 <= T <= 200

1 <= len(S) <= 103

'a' <= S[i] <= 'z'



General Constraints

'a' <= S[i] <= 'z'



Example

Input

5

8

pfyafafd

9

sllwffoqq

6

yoogvb

4

hcch

23

mzmqnnrkurfmmfrukrnnqsm



Output

3

2

2

4

18



Explanation



Self Explanatory

a=int(input())
while a>0:
    n=int(input())
    b=input()
    ans=0
    for i in range(0,n):
        p1=i
        p2=i
        while (p1>=0 and p2<n) and b[p1]==b[p2]:
            p1-=1
            p2+=1
        ans=max(ans,p2-p1-1)
        p3,p4=i,i+1
        while (p3>=0 and p4<n) and b[p3]==b[p4]:
            p3-=1
            p4+=1
        ans=max(ans,p4-p3-1)
    print(ans)
    a-=1