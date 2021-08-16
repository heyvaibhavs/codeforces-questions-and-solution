#include <bits/stdc++.h>
using namespace std;
int main()
{
    int t;
    cin>>t;
    while (t-->0)
    {
        long long x;
        cin>>x;
        long long i=1;
        int z=0;
        while (x-i*i*i>0)
        {
            double t=cbrt(x-i*i*i);
            // cout<<t<<endl;
            if (t-int(t)==0)
            {
                z=-1;
                break;
            }
            i++;
        }
        if (z==-1)
            cout<<"YES"<<endl;
        else
            cout<<"NO"<<endl;
    }
}