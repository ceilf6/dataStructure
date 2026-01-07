N=int(input())

def pan(n):

    if n=='4'or n=='8':#操蛋的特殊情况！
        return 1

    ln=len(n)

    for i in range(ln):
        for j in range(ln):
            if i!=j:
                num=int(n[i]+n[j])
                if num%4==0:
                    return 1

    return 0

for i in range(N):
    n=input()
    if pan(n):
        print('YES')
    else:
        print('NO')
