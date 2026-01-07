t=int(input())

def ans(i,l,m,k,n):
    summ=0
    kleft=k
    mleft=m
    if l[i]==1:
        kleft-=1
    else:
        kleft-=1
        mleft-=1
    j=1
    while kleft>0:
        if i-j>=0 and i+j<=n-1:
            if l[i-j] or l[i+j]:
                if l[i-j]:
                    kleft-=1
                    summ+=j
                    if kleft==0:
                        break
                    if l[i+j]:#两个都行
                        kleft-=1
                        summ+=j
                        if kleft==0:
                            break
                    else:#一个
                        if mleft>0:
                            kleft-=1
                            mleft-=1
                            summ+=j
                            if kleft==0:
                                break
                else:#一个
                    if mleft:
                        kleft-=1
                        summ+=j
                        if kleft==0:
                            break
                        kleft-=1
                        mleft-=1
                        if kleft==0:
                            break
            else:#两个都不行
                if mleft:
                    kleft-=1
                    mleft-=1
                    summ+=j
                    if kleft==0:
                        break
                if mleft:
                    kleft-=1
                    mleft-=1
                    summ+=j
                    if kleft==0:
                        break
        else:#只有一个在里面
            if i-j>=0:
                if l[i-j]:
                    kleft-=1
                    summ+=j
                    if kleft==0:
                        break
                elif mleft:
                    kleft-=1
                    summ+=j
                    if kleft==0:
                        break
            else:
                if l[i+j]:
                    kleft-=1
                    summ+=j
                    if kleft==0:
                        break
                elif mleft:
                    kleft-=1
                    summ+=j
                    if kleft==0:
                        break
        j+=1
    return summ
            
for _ in range(t):
    n,m,k=map(int,input().split())
    l=list(map(int,input()))
    for i in range(n):
        print(ans(i,l,m,k,n),end=' ')
    print()
    
