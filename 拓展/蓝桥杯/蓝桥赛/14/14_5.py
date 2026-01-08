D=int(input())

s=[[] for i in range(D)]
d=[-1]*D
for i in range(D):
    s[i].append(input())#二进制得用字符串形式输入，否则会吞0
    s[i].append(input())

    
    l=len(s[i][0])
    e1=int(s[i][0],2)
    e2=int(s[i][1],2)
    e=e1^e2
    #print(e)

    d[i]=bin(e)[2:].zfill(l)[-l:]
    #d[i]=int(str(s[i][0]^s[i][1]),2)

#print(d)

for i in d:
    #print(i)
    if i[0]=='1' or i[-1]=='1':
        print(-1)
        
    else:
        flag=1
        for k in range(1,len(i)):
            if i[k]=='1' and i[k-1]=='1':
                print(-1)
                flag=0
                break
            
        if flag:
            summ=0
            for j in i:
                if j=='1':
                    summ+=1
            print(summ)
