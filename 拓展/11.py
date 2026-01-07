T=int(input())

def kmp(f,s):
    fs=f+'#'+s
    lf=len(f)
    l=len(fs)
    p=[0]*l
    j=0
    for i in range(1,l):
        while j>0 and fs[i]!=fs[j]:
            j=p[j-1]
        if fs[i]==fs[j]:
            j+=1
        p[i]=j

        if p[i]==lf:
            return 1
    return 0

#-----------------
def build_kmp(s):
    l=len(s)
    nxt=[0]*l
    j=0
    for i in range(1,l):
        while j>0 and s[i]!=s[j]:
            j=nxt[j-1]
        if s[i]==s[j]:
            j+=1
        nxt[i]=j
    return nxt

def match_kmp(f,s,nxt):
    #nxt=build_kmp(s)
    j=0
    l1=len(s)
    l2=len(f)
    for i in range(l2):
        while j>0 and f[i]!=s[j]:
            j=nxt[j-1]
        if f[i]==s[j]:
            j+=1
        if j==l1:
            return 1
    return 0

for _ in range(T):
    n=int(input())

    a,c=input().split()

    nxta=build_kmp(a)
    nxtc=build_kmp(c)

    ans=[]

    for k in range(n):

        b,b2=input().split()
        #if kmp(b,a) and kmp(c,b2):
        #if b in a and c in b2:
        if match_kmp(a,b,nxta) and kmp(c,b2):#match_kmp(c,b2,nxtc):
            ans.append(k+1)

    print(*ans)

    
