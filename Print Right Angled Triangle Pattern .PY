Print Right Angled Triangle Pattern 

Print a mirror image of a right-angled triangle using '*'. See examples for more details.

Input Format

The First line of input contains T - the number of test cases. It's followed by T lines, each line contains a single integer N - the size of the pattern.

Output Format

For each test case, print the test case number as shown, followed by the pattern, separated by a new line.

Constraints

1 <= T <= 100
1 <= N <= 100

Example

Input

4
2
1
5
10


Output

Case #1:
 *
**
Case #2:
*
Case #3:
    *
   **
  ***
 ****
*****
Case #4:
         *
        **
       ***
      ****
     *****
    ******
   *******
  ********
 *********
**********
Explanation
Self Explanatory

a=int(input())
for p in range(1,a+1):
    b=int(input())
    print("Case #%d:"%p)
    for i in range(1,b+1):
        for j in range(b,i,-1):
            print(" ",end="")
        for k in range(0,i):
            print("*",end='')
        print()