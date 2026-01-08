a,b,w=map(int,input().split())

if a==b or b==w or a==w or a+b==w or a+w==b or b+w==a:
    print('YES')
else:
    print('NO')
