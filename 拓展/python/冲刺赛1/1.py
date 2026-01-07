N=int(input())

n=list(map(int,input().split()))

n.sort()

print(' '.join(map(str,n)))
