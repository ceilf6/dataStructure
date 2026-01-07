m,n=map(int,input().split())

s1=set(map(int,input().split()))
s2=set(map(int,input().split()))

s3=s2.intersection(s1)

for i in s1:
    if i in s3:
        print(i,end=' ')
