n,k=map(int,input().split())#贪心不行，得dp

a=list(map(int,input().split()))


for i in range(k):
    if a[0]==a[-1]:
        flag=0
        for j in range(len(a)//2):
            if a[-1-j]>a[j]:
                flag=1
                break
        if flag:
            del a[0]
        else:
            del a[-1]
    elif a[0]>a[-1]:
        del a[-1]
    elif a[-1]>a[0]:
        del a[0]

print(sum(a))
