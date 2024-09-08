Maximum Subarray Sum 
Given an array of integers, find the maximum subarray sum.



Input Format

The first line of input contains T - number of test cases. It is followed by 2T lines. First line of each test case contains N - size of the array and the second line contains N integers - elements of the array.



Output Format

For each test case, print the maximum subarray sum, followed by the start and end indices of the subarray, separated by new line. If multiple subarrays give the same sum, consider the lexicographically smaller one for the answer.



Constraints

20 points

1 <= T <= 100

1 <= N <= 102



30 points

1 <= T <= 100

1 <= N <= 103



50 points

1 <= T <= 100

1 <= N <= 104



General Constraints

-103 <= A[i] <= 103



Example

Input

3

9

-24 0 28 28 55 -31 -27 -45 -24

10

40 5 39 45 31 -44 73 -16 -31 27

7

57 18 -14 17 31 16 -16



Output

111 1 4

189 0 6

125 0 5



Explanation



Self Explanatory




#include <bits/stdc++.h>
using namespace std;
void maxs(int *arr,int n){
    int max_s=-1000,max_e=0;
    int start=0,end=0,s=0;
    for(int j=0;j<n;j++){
        max_e+=arr[j];
        if(max_s<max_e){
            max_s=max_e;
            start=s;
            end=j;
        }
        if(max_e<0){
            max_e=0;
            s=j+1;
        }
    }
    cout<<max_s<<" "<<start<<" "<<end<<endl;
}
int main() {
    int q;
    cin>>q;
    for(int i=0;i<q;i++){
        int n;
        cin>>n;
        int arr[n];
        for(int j=0;j<n;j++) cin>>arr[j];
        maxs(arr,n);
    }
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */   
    return 0;
}