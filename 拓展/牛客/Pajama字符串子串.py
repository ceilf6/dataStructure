n=int(input())#n个用例

s=[[0]*2 for i in range(n)]

for i in range(n):
    s[i][0]=int(input())
    s[i][1]=input()


s1='u'
s2='uwawauwa'

j2=len(s2)-1
#找到后面的，然后找前面u有几个
for i in range(n):
    m=0
    k=[]
    j2=len(s2)-1

    pre=[0]*(s[i][0]+1)
    for t in range(s[i][0]):
        if s[i][1][t]=='u':
            pre[t+1]=pre[t]+1
        else:
            pre[t+1]=pre[t]
    
    for j in range(s[i][0]-1,-1,-1):
        #print(s[i][1][j])
        if s[i][1][j] == s2[j2]:
            j2-=1
        elif j2==-1:
            k.append(j)
            j2=len(s2)-1
            
        else:
            j2=len(s2)-1
            if s[i][1][j] == s2[j2]:
                j2-=1
    #print(k)   至少隔一个
    for kn in range(len(k)):
        m+=pre[k[kn]]
        
    print(m)
