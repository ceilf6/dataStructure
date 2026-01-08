n,x=map(int,input().split())

s=input()


'''
for i in range(len(s)-1):
    for j in range(len(s)-1-i):
        if s[i]<s[j]:
'''         

s2=sorted(s)


flag=0#全部初始糖一致
if s2.count(s2[0])<x:
    flag=1

if flag==0:
    flag2=0
    if s2[-1]==s2[x]:
        flag2=1
    s3=''
    if flag2:
        '''
        for i in range(x-1,len(s2)):
            s3+=s2[i]
        print(s3)
        '''
        ans=''.join(s2[i] for i in range(x-1,len(s2)))
        print(ans)

    else:
        '''
        for i in range(x-1,len(s2),x):
            s3+=s2[i]
        '''
        ans=''.join(s2[i] for i in range(0,len(s2),x))#得从头开始！不然娶不到后面的
        print(ans)
else:
    print(s2[x-1])
