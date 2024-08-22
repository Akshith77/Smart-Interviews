Balanced Parentheses 
Write a program to generate all possible strings with balanced parentheses having N pairs of curly braces.



Input Format

The first line of input contains T - the number of test cases. It's followed by T lines, each containing a single integer N.



Output Format

For each test case, print each combinational pair of balanced parenthesis of length N in a lexicographical order along with the test case number, separated by a new line.



Constraints

1 <= T <= 12

1 <= N <= 12



Example

Input

2

3

2



Output

Test Case #1:
{{{}}}
{{}{}}
{{}}{}
{}{{}}
{}{}{}
Test Case #2:
{{}}
{}{}


Explanation



Self Explanatory

#include <bits/stdc++.h>
using namespace std;
void balpal(char a[],int oc,int cc,int idx,int n){
    if(idx==n){
        for(int j=0;j<n;j++){
                printf("%c",a[j]);
        }
        printf("\n");
        return;
    }
    if(oc<n/2){
        a[idx]='{';
        balpal(a,oc+1,cc,idx+1,n);
    }
    if(cc<oc){
        a[idx]='}';
        balpal(a,oc,cc+1,idx+1,n);
    }
}

int main() {
    int t;
    scanf("%d",&t);
    for(int i=1;i<=t;i++){
        int m,n;
        scanf("%d",&m);
        n=2*m;
        char a[n];
        printf("Test Case #%d:\n",i);
        balpal(a,0,0,0,n);
    }
    return 0;
}