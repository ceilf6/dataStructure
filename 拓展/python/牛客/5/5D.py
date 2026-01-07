import math

n=int(input())
s=input()
ls=len(s)

anss=[]

for i in range(1,n+1):
    t=math.ceil(ls/i)#总共有t段

    ans=1
    for j in range(t-1):#前t-1段
        s2=s[j*i:j*i+i]#注意：每段开头是j*i

        for a in s2[1:]:
            if a!=s2[0]:
                ans+=1
                break

    for a in s[(t-1)*i:]:#要用i求得最后一段开头啊！
        if a!=s[(t-1)*i]:
            ans+=1
            break


    anss.append(ans)


ansss=anss[0]
for i in anss[1:]:
    ansss^=i


print(ansss)
