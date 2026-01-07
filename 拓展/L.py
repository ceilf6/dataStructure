T=int(input())

for _ in range(T):

    pre1=0
    pre0=0

    s=input()

    pre10=[0]
    pre01=[0]

    ls=len(s)

    for i in range(ls):
        if s[i]=='1':
            pre01.append(pre01[-1]+1)
        else:
            pre01.append(pre01[-1])

        if s[ls-1-i]=='0':
            last10=[last10[0]+1]+last10
        else:
            last10=[last10[0]]+last10

    print(pre01,last10)
