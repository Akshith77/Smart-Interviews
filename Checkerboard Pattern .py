Checkerboard Pattern 
You are given an integer N. Print a 2N×2N checkerboard consisting of 2×2 squares alternating '*' and '-', with the top-left cell being '*'. See the following examples for N = 1,2,3 and 4 respectively.



  N = 1           N = 2                      N = 3


              N = 4
Input Format

The first line of input contains T - the number of test cases. It is followed by T lines, each line contains a single integer N - the size of the pattern.



Output Format

For each test case, print the test case number as shown, followed by the pattern, separated by a new line.



Constraints

1 <= T <=100

1 <= N <=100



Example

Input

2

4

2



Output

Case #1:
**--**--
**--**--
--**--**
--**--**
**--**--
**--**--
--**--**
--**--**
Case #2:
**--
**--
--**
--**
Explanation



Self Explanatory


# Enter your code here. Read input from STDIN. Print output to STDOUT
q=int(input())
for i in range(1,q+1):
    n=int(input())
    print("Case #%d:"%i)
    a=0
    for i in range(1,2*n+1):
        if a<2:
            for j in range(1,n+1):
                if j%2==0:
                    print("--",end="")
                else:
                    print("**",end="")
            print()
            a+=1
        else:
            for j in range(1,n+1):
                if j%2==0:
                    print("**",end="")
                else:
                    print("--",end="")
            print()
            a+=1
        if a==4:
            a=0