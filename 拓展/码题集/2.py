
def main():
    #code here
    n,q=map(int,input().split())
    a=list(map(int,input().split()))
    '''
    s=[a[0]]
    for i in range(1,len(a)):
        s.append(s[-1]+a[i])
    '''
    s=[a[-1]]
    for i in range(len(a)-2,-1,-1):
        s=[s[0]+a[i]]+s

    s2=[s[0]]
    for i in range(1,len(s)):
        s2.append(s2[-1]+s[i])
    #print(s)
    #print(s2)
    for _ in range(q):
        l,r=map(int,input().split())
        '''
        ans=0
        for j in range(l-1,r): # l,r是从1开始的
            #print(j)
            ans=(ans+s[r-1]-s[j-1])%998244353
        print(ans)
        '''
        if l>=2:print(s2[r-1]-s2[l-2])
        else:print(s2[r-1])
    pass


if __name__ == '__main__':
    main();
