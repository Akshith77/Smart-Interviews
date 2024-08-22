Rearrange Sequence - 1 
You are given an array of size N containing unique integers. Find the size of the largest subarray that can be rearranged to form a contiguous sequence.

A contiguous sequence means that the difference of adjacent elements should be 1.



Input Format

The first line of input contains T - the number of test cases. It's followed by 2T lines, the first line contains N - the size of the array. The second line contains the elements of the array.



Output Format

For each test case, print the size of the largest subarray that can be rearranged to form a contiguous sequence, on a new line.



Constraints

30 points

1 <= T <= 100

4 <= N <= 100



70 points

1 <= T <= 100

4 <= N <= 1000



General Constraints

0 <= A[i] <= 105



Example

Input

2

5

1 3 2 6 5

9

0 8 6 5 7 10 3 2 1



Output

3

4



Explanation



Test-Case 1

The largest subarray that can be rearranged to form a contiguous sequence is [1, 3, 2] which can be rearranged to form [1, 2, 3].



Test-Case 2

The largest subarray that can be rearranged to form a contiguous sequence is [8, 6, 5, 7] which can be rearranged to form [5, 6, 7, 8].






#include <bits/stdc++.h>
using namespace std;
bool valid(vector<int> temp,int n){
    sort(temp.begin(),temp.end());
    for(int i=1;i<n;i++){
        if(temp[i]-temp[i-1]!=1){
            return false;
        }
    }
    return true;
}
long func(long ar[],long n){
long ans=1;
    for(long i=0;i<n;i++)
    {
        vector<int> temp;
        for(long j=i;j<n;j++){
            temp.push_back(ar[j]);
            if (valid(temp,n)){
                sort(temp.begin(),temp.end());
                ans=max(ans,temp[temp.size()-1]);
            }
        }
    }
    return ans;
}
int main() {
    long a;
    cin>>a;
    while(a--){
        long b;
       cin>>b;
       int ar[b];
       for(int i=0;i<b;i++){
           cin>>ar[i];
       } 
       cout<<func(ar,b);
    }
    return 0;
}