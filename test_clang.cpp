#include<bits/stdc++.h>
using namespace std;
int main()
{
    vector<string> v;
    string s="cat dog cat dog";
    string s1="";
    for(int i=0;i<s.size();i++)
    {
        if(s[i] != ' ')
            s1+=s[i];
        else
        {
            v.push_back(s1);
            s1="";
        }

    }
    v.push_back(s1);
    for(int i=0;i<v.size();i++)
        cout<<v[i]<<" ";
    return 0;
}