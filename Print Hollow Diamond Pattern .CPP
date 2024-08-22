Print Hollow Diamond Pattern 
Print a hollow diamond pattern using '*'. See examples for more details.



Input Format

The first line of input contains T - the number of test cases. It is followed by T lines, each line contains a single odd integer N - the size of the diamond.



Output Format

For each test case, print the test case number as shown, followed by the diamond pattern, separated by a new line.



Constraints

1 <= T <= 100

3 <= N <= 201



Example

Input

4
3
7
5
15


Output

Case #1:
 *
* *
 *
Case #2:
   *
  * *
 *   *
*     *
 *   *
  * *
   *
Case #3:
  *
 * *
*   *
 * *
  *
Case #4:
       *
      * *
     *   *
    *     *
   *       *
  *         *
 *           *
*             *
 *           *
  *         *
   *       *
    *     *
     *   *
      * *
       *
Explanation
Self Explanatory

#include <bits/stdc++.h>
using namespace std;

int main() {
    int n,a;
    cin>>a;
    for(int g=0;g<a;g++){
        cin>>n;
        cout<<"Case #"<<g+1<<":"<<endl;
        for(int i=0;i<n/2;i++){
            for(int j=n/2;j>i;j--){
                cout<<" ";
            }
            cout<<"*";
            for(int k=1;k<i;k++){
                cout<<" ";
            }
            for(int k=1;k<=i;k++)
            {
                cout<<" ";
            }
            if(i>0){
                cout<<"*";
            }
            cout<<endl;
        }
            for(int i=0;i<n/2+1;i++){
            for(int j=0;j<i;j++){
                cout<<" ";
            }
            cout<<"*";
            for(int k=i;k<n/2;k++){
                cout<<" ";
            }
            for(int k=i+1;k<n/2;k++)
            {
                cout<<" ";
            }
            if(i!=n/2){
                cout<<"*";
            }
            cout<<endl;
        }
    }
    return 0;
}