t=int(input())

for i in range(t):
    p=input()
    s=input()

    s=s.replace('LL','L')
    s=s.replace('RR','R')

    if s==p:
        print('YES')
    else:
        print('NO')
    
