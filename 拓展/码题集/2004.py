n=list(map(int,input()))
l=len(n)
l_2=l//2
for i in range(l_2):
    '''
    if n[i]<n[l-1-i]:
        n[l-1-i]=n[i]
    '''
    if n[i]>n[l-1-i]:
        k=l-1-i-1
        while k>=i:
            if n[k]>=1:
                n[k]-=1
                for j in range(k+1,l-1-k):
                    n[j]=9

                break
            k-=1

    n[l-1-i]=n[i]

if n[0]==0:
    print('9'*(l-1))
else:
    print(''.join(map(str,n)).lstrip('0'))
