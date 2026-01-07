n=int(input())

a=list(map(int,input().split()))

a.sort()

m=a[n//2]

maxx=max(m-ai for ai in a)
minn=max(ai-m for ai in a)

tot=maxx+minn

print(tot,m)
