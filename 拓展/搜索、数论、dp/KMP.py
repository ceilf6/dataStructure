from collections import Counter

fs=input()


def prentx(fs):
    l=len(fs)
    p=[0]*l
    j=0
    for i in range(1,l):
        while j>0 and fs[i]!=fs[j]:
            j=p[j-1]
        if fs[i]==fs[j]:
            j+=1
        p[i]=j
    return p


P=prentx(fs)

maxx=P[-1]
flag=0
while maxx:
    f=fs[:maxx]

    if f in fs[1:-1]:
        print(f)
        flag=1
        break

    maxx-=1

if flag==0:
    print("Hello KMP!")

    

