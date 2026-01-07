n,d,m,l=map(int,input().split())

# 注意是第一个不被覆盖的点，而不是能到达的最远
rmin=1
lmax=1
now=1

while rmin>=lmax:
    print((now-1)*m,(now-1)*m+l)
    rmin=lmax+l
    lmax=max(lmax,(now-1)*m+l)
    now+=d


print(rmin+1)




'''
# 要利用 +l 的性质

lmax=1
now=1
while now<
'''

'''
ma=1
mi=1
now=1

while mi<=now<=ma:
    print((now-1)*m,(now-1)*m+l)
    mi=max(mi,(now-1)*m)
    ma=max(ma,(now-1)*m+l)
    now+=d

print(ma)
'''
