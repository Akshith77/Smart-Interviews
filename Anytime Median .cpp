Anytime Median 
Given an integer array, print the median for the sub-array 0 to i, for every i, 0 <= i <= N-1.



Input Format

The first line of input contains T - the number of test cases. It's followed by 2T lines - the first line contains N - the size of the array. The second line contains N integers - the elements of the array.



Output Format

For each test case, print the median for the sub-array 0 to i, for every i, separated by space. Print a new line between the output of different test cases. Note that in the case of even length sub-array, print the smaller element as the median.



Constraints

30 points

1 <= T <= 100

1 <= N <= 103



70 points

1 <= T <= 100

1 <= N <= 104



General Constraints

-104 <= A[i] <= 104



Example

Input

2

5

-10 14 11 -5 7 

3

2 -5 14 



Output

-10 -10 11 -5 7 

2 -5 2 



Explanation



Self Explanatory



#include <bits/stdc++.h>
using namespace std;
int printmed(int *ar,int n){
    priority_queue <int, vector<int>,greater<int>> mi;
    priority_queue <int> ma;
    ma.push(ar[0]);
    cout<<ma.top()<<" ";
    for(int i=1;i<n;i++){
        if(ar[i]<=ma.top()){
            ma.push(ar[i]);
            if(ma.size()-mi.size()>1){
                mi.push(ma.top());
                ma.pop();
            }
        }
        else if(ar[i]>ma.top())
        {
            mi.push(ar[i]);
            if(mi.size()>ma.size()){
                ma.push(mi.top());
                mi.pop();
            }
        }
        cout<<ma.top()<<" ";
    }
}
int main() {
    int t;
    cin>>t;
    while(t--){
        int n;
        cin>>n;
        int ar[n];
        for(int i=0;i<n;i++) cin>>ar[i];
        printmed(ar,n);
        cout<<endl;
    }
     return 0;
}