n,d = map(int,input().split())

a = list(map(int,input().split()))

import math
h = math.floor(d/400)

#if(h==2):

npre = 0

naft = 0

for i in a:
    if i > h:
        npre+=1
    elif i < h:
        naft+=1

teshu = [399,799]      
if(d in teshu):
    print(npre+1,npre+1)
else:
    print(npre+1,n-naft)
