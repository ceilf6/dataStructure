fo,b,a1,a2=map(int,input().split())

flag1=0
flag2=0
if b>a1>=fo:
    flag1=1
elif a1>=b:
    flag1=2

if b>a2>=fo:
    flag2=1
elif a2>=b:
    flag2=2
    
if not flag1 and not flag2:
    print('zhang da zai lai ba')
elif not flag1 and flag2==1:
    print('2: huan ying ru guan')
elif not flag2 and flag1==1:
    print('1: huan ying ru guan')
elif not flag1 and flag2==2:
    print('qing 2 zhao gu hao 1')
elif not flag2 and flag1==2:
    print('qing 1 zhao gu hao 2')
elif flag2>=1 and flag1>=1:
    print('huan ying ru guan')
