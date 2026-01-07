n,m=map(int,input().split())

k=list(map(int,input().split()))

M=[]

for i in range(m):
    M.append(int(input()))


def dfs(step,a,b,mi):
    global flag
    
    if flag:
        return

    if step==n:
        summ=sum(a)*sum(b)
            
        if summ==mi:
            print('Yes')
            print(len(a),len(b))
            for i in a:
                print(i,end=' ')
            print()
            for j in b:
                print(j,end=' ')
            print()
            flag=1
        return

    a2=a.copy()
    a2.append(k[step])
    dfs(step+1,a2,b,mi)

    b2=b.copy()
    b2.append(k[step])
    dfs(step+1,a,b2,mi)

    dfs(step+1,a,b,mi)


for mi in M:
    flag=0
    
    dfs(0,[],[],mi)

    if not flag:
        print('No')

        
