from collections import Counter

N=int(input())

s0='CHICKEN'
ls0=len(s0)
for i in range(N):
    n=int(input())
    s=input()

    p=0
    q=0
    flag=0
    while q<n:
        if s[q]==s0[p]:
            p+=1
            s=s[:q]+s[q+1:]
            q-=1 #抵消!
        if p==ls0:
            flag=1
            break
        q+=1

    #print(s)
    if flag==0:
        print('NO')
    else:
        if len(s)%2==1:
            print('NO')
        else:
            '''
            t=0
            dictt={}
            count=[0]*100
            for i in s:
                if i in dictt:
                    count[dictt[i]]+=1
                    continue
                else:
                    dictt[i]=t
                    count[dictt[i]]+=1
                    t+=1
'''
            count=Counter(s)
            count2=sorted(count.values(), reverse=True)
            while sum(1 for x in count if x!=0)>1:
                count2.sort(reverse=1)
                #print(count)
                count2[0]-=count[1]
                count2[1]=0

            if count2[0]==0:
                print('YES')
            else:
                print('NO')
            
                


