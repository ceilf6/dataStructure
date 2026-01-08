N=int(input())

a=list(map(int,input().split()))

b=[0]*(N//2)

for i in range(1,N//2+1):
    b[i-1]=a[i-1]-a[-i]

print(b)

def min_operations(nums):
    n = len(nums)
    d = nums.copy()
    operations = 0
    for i in range(n):
        while d[i] != 0:
            if i + 1 < n and d[i] * d[i + 1] > 0:
                # 符号相同，可以双操作
                k = min(abs(d[i]), abs(d[i + 1]))
                operations += k
                if d[i] > 0:
                    d[i] -= k
                    d[i + 1] -= k
                else:
                    d[i] += k
                    d[i + 1] += k
            else:
                # 单独处理当前元素
                operations += abs(d[i])
                d[i] = 0
    return operations


print(min_operations(b))

'''
maxx=max(b)
f=-1

def judge():
    for i in b:
        if i!=0:
            return 1
    return 0

summ=0
while judge():
    for i in range(N//2):
        if a[i]==maxx:
            f=i
            break

    if a[i+1]>a[i-1]:
        summ+=a[i+1]
        a[i]-=a[i+1]
        a[i+1]=0
    else:
        summ-=a[i+1]
        a[i]-=a[i-1]
        a[i-1]=0

print(summ)
'''
