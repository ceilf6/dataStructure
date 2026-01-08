from math import sqrt
from math import factorial
n=int(input())

a=list(map(int,input().split()))

maxa=max(a)
'''
f=[1,1]

for i in range(2,maxa+1):
    f.append(f[-1]*i)


k=0
for i in a:
    k+=f[i]

F=f[-1]

del f
'''

k=0

for i in a:
    k+=factorial(i)


#I=maxa

I=1
F=1

while F<sqrt(k):
    I+=1
    F*=I


flag=0
while 1:
    if k%F==0:     
        print(I)
        break
    F/=I
    I-=1
