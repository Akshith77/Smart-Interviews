Subsequence Sum 
Given a sequence of N numbers: S1, ..., SN, determine how many subsequences of S have a sum between A and B inclusive.



Input Format

The first line of input contains T - the number of test cases. It's followed by 2T lines, the first line contains - N, A, and B separated by space. The next line contains the sequence of N numbers.



Output Format

For each test case, print the result, separated by a new line.



Constraints

30 points

1 <= T <= 100

1 <= N <= 15



120 points

1 <= T <= 100

1 <= N <= 30



General Constraints

-107 <= A <= B <= 107

-107 <= S[i] <= 107



Example

Input

2

3 -1 2

1 -2 3

5 5 15

1 4 -3 6 4



Output

5

20



Explanation



Self Explanatory


# Enter your code here. Read in
def check(n,k):
    return n&(1<<k)

def generated(arr):
    res=[]
    for i in range(1<<len(arr)):
        temp=0
        for j in range(len(arr)):
            if check(i,j):
                temp+=arr[j]
        res.append(temp)
    return res

def searchlower(arr,lb):
    low=0
    high=len(arr)
    while low<high:
        mid=(high+low)//2
        if lb<=arr[mid]:
            high=mid
        else:
            low=mid+1
    return low

def searchup(arr,ub):
    low=0
    high=len(arr)
    while low<high:
        mid=(high+low)//2
        if ub>=arr[mid]:
            low=mid+1
        else:
            high=mid
    return low

for _ in range(int(input())):
    n,a,b=map(int,input().split())
    arr=list(map(int,input().split()))
    sub1=generated(arr[:(n//2)+1])
    sub2=sorted(generated(arr[(n//2)+1:]))
    c=0
    for i in sub1:
        low=searchlower(sub2,a-i)
        up=searchup(sub2,b-i)
        c+=(up-low)
    print(c)