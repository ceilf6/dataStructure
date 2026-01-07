t=int(input())

for i in range(t):
    flag=0
    s=input()
    p=input()

    lcnt=p.count('LL')
    rcnt=p.count('RR')

    if s==p:
        flag=1

    elif lcnt and rcnt:
        for i in range(lcnt+1):
            if flag:
                break
            for j in range(rcnt+1):
                p2=p.replace('LL','L',i)
                p2=p2.replace('RR','R',j)

                if p2==s:
                    flag=1
                    break
    elif lcnt:
        for i in range(lcnt+1):
            p2=p.replace('LL','L',i)
            if p2==s:
                flag=1
                break
    elif rcnt:
        for j in range(rcnt+1):
            p2=p.replace('RR','R',j)
            if p2==s:
                flag=1
                break
        

    if flag:
        print('YES')
    else:
        print('NO')
