def KMP(f,s):
    fs=f+'#'+s

    l=len(fs)
    lf=len(f)
    j=0
    p=[0]*l
    for i in range(1,l):
        while j>0 and fs[i]!=fs[j]:
            j=p[j-1]
        if fs[i]==fs[j]:
            j+=1
        p[i]=j
        
        if p[i]==lf:
            start=i-2*lf
            return start
    return -1
f=input()
s=input()
print(KMP(f,s))
