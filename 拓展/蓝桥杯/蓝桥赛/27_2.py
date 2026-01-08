s=input()
ls=len(s)

dp=[[0]*3 for i in range(ls)]

dp[0][0]=(s[0]=='l')
#print(dp)
#dp
for i in range(1,ls):
    dp[i][0]=dp[i-1][0]+(s[i]=='l')
    dp[i][1]=dp[i-1][1]+dp[i-1][0]*(s[i]=='a')
    dp[i][2]=dp[i-1][2]+dp[i-1][1]*(s[i]=='n')


print(dp[-1][-1])






sl=[0]*ls#前缀和
sn=[0]*ls#后缀和


sl[0]=int(s[0]=='l')
sn[-1]=int(s[-1]=='n')

for i in range(1,len(s)):
    sl[i]=sl[i-1]+(s[i]=='l')
    sn[-i-1]=sn[-i]+(s[-i-1]=='n')
'''
print(sl)
print(sn)
'''
ans=0
for i in range(len(s)):
    if s[i]=='a':
        ans+=sl[i]*sn[i]
#print(ans)






s='lan'
dic={}
for i in range(len(lan)):
    if lan[i] in s:
        if lan[i] in dic:
            dic[lan[i]].append(i)
        else:
            dic[lan[i]]=[i]

ans=0
#print(dic)

      

'''
for i in dic['l']:
    for j in dic['a']:
        if i>=j:
            continue
        for z in dic['n']:
            #print(i,j,z)
            if z<=j:
                continue
            if i<j<z:
                ans+=1

'''
def dfs(step,ze):
    global ans
    if step>=1:
        if ze[step]<ze[step-1]:
            return

    if step==2:
        ans+=1
        #print(ze)
        return

    new_ze=ze.copy()
    for i in dic[s[step+1]]:
        new_ze.append(i)
        dfs(step+1,new_ze)
        new_ze=ze.copy()
        
    

dfs(-1,[])
print(ans)

