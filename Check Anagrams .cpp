Check Anagrams 
Given 2 strings, check if they are anagrams. An anagram is a rearrangement of the letters of one word to form another word. In other words, some permutations of string A must be the same as string B.



Input Format

The first line of input contains T - the number of test cases. It's followed by T lines, each line containing 2 space-separated strings.



Output Format

For each test case, print True/False, separated by a new line.



Constraints

10 points

1 <= T <= 100

1 <= len(S) <= 103

'a' <= S[i] <= 'z'



40 points

1 <= T <= 100

1 <= len(S) <= 105

'a' <= S[i] <= 'z'



Example

Input

4

iamlordvoldemort tommarvoloriddle

b h

stop post

hi hey



Output

True

False

True

False



Explanation



Self Explanatory


#include <bits/stdc++.h>
using namespace std;
bool Anagrams(const string &s1,const string &s2){
    if(s1.length()!=s2.length()){
        return false;
    }
    vector<int> count(26,0);
    for(char ch:s1){
        count[ch-'a']++;
    }
    for(char ch:s2){
        count[ch-'a']--;
    }
    for(int i=0;i<26;i++){
        if(count[i]!=0){
            return false;
        }

    }
    return true;
}
int main() {
    int n;
    cin>>n;

string a;
string b;
while(n--){
    cin>>a>>b;
    if(Anagrams(a,b)){
        cout<<"True"<<endl;
    }
    else{
        cout<<"False"<<endl;
    }
}


    return 0;
}