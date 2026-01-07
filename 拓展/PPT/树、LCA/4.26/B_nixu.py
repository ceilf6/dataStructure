n=int(input())
a=list(map(int,input().split()))
b=list(map(int,input().split()))

def ni(lis):
    le=len(lis)
    cnt=0
    for i in range(le):
        
        for j in range(i+1,le):
            if lis[i]>lis[j]:
                cnt+=1
    return cnt

print(ni(a)+ni(b))
