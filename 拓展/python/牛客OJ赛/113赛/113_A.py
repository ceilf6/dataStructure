s=input()


summ=1
flag=0
i=0
while i<len(s) and not flag:
    if s[i]=='-':
        summ-=1
    elif s[i]=='*':
        summ*=2

    if summ>=2025:
        print('YES')
        flag=1
        break
    i+=1
if not flag:
    print('NO')
