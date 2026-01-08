fo,b,a1,a2=map(int,input().split())
p1=a1>=fo or(a1<fo and a2>=b)
p2=a2>=fo or(a2<fo and a1>=b)
print(f"{a1}-{'Y'if p1 else'N'} {a2}-{'Y'if p2 else'N'}")
if not p1 and not p2:
    print("zhang da zai lai ba")
elif p1 and p2:
    d1=a1<fo and a2>=b
    d2=a2<fo and a1>=b
    if d1 or d2:
        if d2:print("qing 1 zhao gu hao 2")
        else:print("qing 2 zhao gu hao 1")
    else:print("huan ying ru guan")
else:
    if p1:print("1: huan ying ru guan")
    else:print("2: huan ying ru guan")
