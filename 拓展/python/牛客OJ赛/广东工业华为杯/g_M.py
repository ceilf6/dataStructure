T=int(input())

from math import factorial

MOD=10**9+7
for i in range(T):
    n,m,k=map(int,input().split())

    
    k=n-k#出去吃
    
    if n>k:
        summ=0
        summ=(summ+factorial(k)/factorial(n-1)/factorial(n-1-k)*m**(k+1)*(m-1)**(n-1-k))%MOD
        
        summ=(summ+factorial(k-1)/factorial(n-2)/factorial(n-2-k)*m**k*(m-1)**(n-k-1))%MOD
        print(summ)
    
        
