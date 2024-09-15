Overlapping Rectangles 
Given 2 rectangles parallel to coordinate axes, find the area covered by them.



Input Format

The first line of input contains T - the number of test cases. It is followed by 2T lines. The first line of each test case contains 4 integers - xbl, ybl, xtr, ytr - the bottom-left and top-right coordinates of rectangle-1. The second line of each test case contains 4 integers - xbl, ybl, xtr, ytr - the bottom-left and top-right coordinates of rectangle-2.



Output Format

For each test case, print the area covered by the 2 rectangles, separated by a newline.



Constraints

1 <= T <= 10000

-106 < x,y <= 106

(xbl, ybl) < (xtr, ytr)



Example

Input

4

2 5 4 6

1 2 5 4

-4 -3 -2 5

-3 -5 1 3

1 0 3 5

2 3 5 8

-2 2 4 4

-3 1 5 5



Output

10

42

23

32



Explanation



Self Explanatory




# Enter your code here. Read input from ST
for _ in range(int(input())):
    x1,y1,x2,y2=map(int,input().split())
    x3,y3,x4,y4=map(int,input().split())
    a1=abs(x1-x2)*abs(y1-y2)
    a2=abs(x3-x4)*abs(y3-y4)
    a3=min(x2,x4)-max(x1,x3)
    a4=min(y2,y4)-max(y1,y3)
    area=0
    if a3>0 and a4>0:
        area=a3*a4
    print(a1+a2-area)  