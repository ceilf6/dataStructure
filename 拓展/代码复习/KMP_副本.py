def KMP(f,s):
    fs=f+'#'+s
    lf=len(f)
    l=len(fs)
    p=[0]*l
    j=0
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

print(KMP('aa','fsdeasdaaa'))
