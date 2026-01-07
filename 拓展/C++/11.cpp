#include<iostream>
#include<vector>
#include<string>
using namespace std;

int main(){
    int T;
    cin>>T;
    while(T--){
        int n;
        cin>>n;
        string a,c;
        cin>>a>>c;
        vector<int>ans;
        for(int k=0;k<n;k++){
            string b,b2;
            cin>>b>>b2;
            if(b.find(a) != string::npos && b2.find(c) != string::npos){
                ans.push_back(k+1);
            }
        }
        for(int i=0;i<ans.size();i++){
            cout<<ans[i];
            if(i+1<ans.size())cout<<" ";
        }
        cout<<endl;
    }
    return 0;
}

/*
int kmp(string f,string s){
    string fs=f+"#"+s;
    int lf=f.size();
    int l=fs.size();
    vector<int>p(l);
    int j=0;
    for(int i=1;i<l;i++){
        while(j>0&&fs[i]!=fs[j]){
            j=p[j-1];
        }
        if(fs[i]==fs[j]){
            j++;
        }
        p[i]=j;
        if(p[i]==lf){
            return 1;
        }
    }
    return 0;
}


///////////////////

vector<int>build_kmp(string s){
    int l=s.size();
    vector<int>nxt(l);
    int j=0;
    for(int i=1;i<l;i++){
        while(j>0&&s[i]!=s[j]){
            j=nxt[j-1];
        }
        if(s[i]==s[j]){
            j++;
        }
        nxt[i]=j;
    }
    return nxt;
}

int match_kmp(string f,string s,vector<int>&nxt){
    int j=0;
    int l1=s.size();
    int l2=f.size();
    for(int i=0;i<l2;i++){
        while(j>0&&f[i]!=s[j]){
            j=nxt[j-1];
        }
        if(f[i]==s[j]){
            j++;
        }
        if(j==l1){
            return 1;
        }
    }
    return 0;
}

int main(){
    int T;
    cin>>T;
    while(T--){
        int n;
        cin>>n;
        string a,c;
        cin>>a>>c;
        vector<int>nxta=build_kmp(a);
        vector<int>nxtc=build_kmp(c);
        vector<int>ans;
        for(int k=0;k<n;k++){
            string b,b2;
            cin>>b>>b2;
            if(match_kmp(a,b,nxta)&&kmp(c,b2)){
                ans.push_back(k+1);
            }
        }
        for(int i=0;i<ans.size();i++){
            cout<<ans[i];
            if(i+1<ans.size())cout<<" ";
        }
        cout<<endl;
    }
    return 0;
}
*/