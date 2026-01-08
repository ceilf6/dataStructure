

import math
N=int(input())

def p(N):
    for i in range(N//2+1):
        for j in range(i,N//2+1):
            for a in range(j,N//2+1):
                b=math.sqrt(N-i**2-j**2-a**2)
                if b==int(b):
                    return (i,j,a,int(b))

for i in p(N):
    print(i,end=' ')
