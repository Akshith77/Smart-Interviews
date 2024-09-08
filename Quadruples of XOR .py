Quadruples of XOR 
You are given 4 arrays of integers: A, B, C, and D. You have to find the number of quadruples (i, j, k, l) such that A[i]^B[j]^C[k]^D[l] = 0, where ^ is the bitwise XOR operator.



Input Format

The first line of input contains T - the number of test cases. It's followed by 5T lines, the first line contains N - the size of the array. The next 4 lines contain the elements of the arrays A, B, C, and D respectively.



Output Format

Print the total number of quadruples for each test case, separated by a new line.



Constraints

10 points

1 <= T <= 100

1 <= N <= 20

1 <= A[i] <= 100



20 points

1 <= T <= 100

1 <= N <= 100

1 <= A[i] <= 100



70 points

1 <= T <= 100

1 <= N <= 500

1 <= A[i] <= 100



Example

Input

3

4

31 8 28 10 

18 7 22 5 

16 25 20 14 

39 9 34 19 

2

27 21 

39 40 

64 77 

36 5 

8

49 73 58 30 72 44 78 23 

9 40 65 92 42 87 3 27 

29 40 12 3 69 9 57 60 

33 99 78 16 35 97 26 12 



Output

2

0

36



Explanation



Test-Case 1

There are only 2 quadruples with XOR=0: 28^22^25^19 and 28^5^16^9.



Test-Case 2

None of the quadruples has XOR=0.



# Enter your code here. Read input from STDIN. Print o
def quad(a,b,c,d,n):
    ab=[]
    cd=[]
    mp=dict()
    co=0
    for i in range(n):
        for j in range(n):
            ab.append(a[i]^b[j])
            cd.append(c[i]^d[j])
            try:
                mp[c[i]^d[j]]+=1
            except:
                mp[c[i]^d[j]]=1
    for i in ab:
        try:
            co+=mp[i]
        except:
            pass
    return co

for _ in range(int(input())):
    n=int(input())
    o=list(map(int,input().split()))
    p=list(map(int,input().split()))
    q=list(map(int ,input().split()))
    r=list(map(int,input().split()))
    print(quad(o,p,q,r,n))