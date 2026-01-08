import math

T=int(input())


a=[0]*T
b=[0]*T
ba=[0]*T
bb=[0]*T
for i in range(T):
    a[i],b[i]=map(int,input().split())

    ba[i]=bin(a[i])[2:]
    bb[i]=bin(b[i])[2:]

for i in range(T):
    a1=ba[i]
    b1=bb[i]

    a2=a1
    b2=b1
    a2=a2.replace('1','2')
    a2=a2.replace('0','1')
    a2=a2.replace('2','0')

    b2=b2.replace('1','2')
    b2=b2.replace('0','1')
    b2=b2.replace('2','0')


    a2h=int(a2,2)
    b2h=int(b2,2)

    mu=[a[i],b[i],a2h,b2h]
    cao=[a[i],b[i]]
    flag=1


    k=[[] for i in range(4)]
    biao=[[0],[0]]
    while flag:
        for i in range(len(cao)):
            for j in range(i+1,len(cao)):
                yu=cao[i]&cao[j]
                huo=cao[i]|cao[j]
                yi=cao[i]^cao[j]
                gcd=math.gcd(cao[i],cao[j])

                if yu in mu:
                    k[0]=[i,j,1,yu]
                    flag=0
                if huo in mu:
                    k[1]=[i,j,2]
                    flag=0
                if yi in mu:
                    k[2]=[i,j,3]
                    flag=0
                if gcd in mu:
                    k[3]=[i,j,4]
                    flag=0

                
                cao.append(yu)
                biao.append([i,j,1])
                cao.append(huo)
                biao.append([i,j,2])
                cao.append(yi)
                biao.append([i,j,3])
                cao.append(gcd)
                biao.append([i,j,4])

    print(mu)    
    print(k)
    print(biao)

                
                    







