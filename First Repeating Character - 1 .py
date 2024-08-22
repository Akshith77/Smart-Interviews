First Repeating Character - 1 
Given a string of characters, find the first repeating character.



Input Format

The first line of input contains T - the number of test cases. It's followed by T lines, each line contains a single string of characters.



Output Format

For each test case, print the first repeating character, separated by a new line. If there are none, print '.'.



Constraints

1 <= T <= 1000

'a' <= str[i] <= 'z'

1 <= len(str) <= 104



Example

Input

4

datastructures

algorithms

smartinterviews

hackerrank



Output

a

.

s

a



Explanation



Self Explanatory



# Enter your code here. Read input from STDIN. Print output to STDOUT
a=int(input())
while a>0:
    b=input()
    c=len(b)
    d=list(set(b))
    e=0
    for i in range(0,len(d)):
        q=d[i]
        if b.count(q)>1:
            e=q
            break
    if e==0:
        print(".")
    else:
        print(e)
    a-=1