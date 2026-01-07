n,m=map(int,input().split())


y=input()
y=y.replace('B','1')
y=y.replace('W','0')
y=int(y,2)
for i in range(n-1):
    inn=input()
    inn=inn.replace('W','0')
    inn=inn.replace('B','1')
    y=y^int(inn,2)

if y:
    print('YES')
else:
    print('NO')
    
    
