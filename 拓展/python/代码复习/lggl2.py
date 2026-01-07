def lggl(s):
    t='#'+'#'.join(s)+'#'

    n=len(t)
    C=R=center=max_len=0
    p=[0]*n

    for i in range(n):
        p[i]=min(p[C*2-i],R-i) if R-i>0 else 0

        while i+p[i]+1<n and i-p[i]-1>=0\
              and t[i+p[i]+1]==t[i-p[i]-1]:
            p[i]+=1

        if R<i+p[i]:
            C,R=i,i+p[i]

        if p[i]>max_len:
            max_len,center=p[i],i

    return s[(center-max_len)//2:(center+max_len)//2]

print(lggl('ssaassass'))
