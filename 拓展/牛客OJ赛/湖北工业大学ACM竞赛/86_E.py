#答案错了:比如2 3 3 5
#枚举组合，然后从后面选尽量小的

T=int(input())

a=[[]for i in range(T)]

for i in range(T):
    n=int(input())
    a[i]=list(map(int,input().split()))
    a[i].sort()
    #print(a[i])
    
for i in range(T):
    if sum(a[i][:len(a[i])-1])<=a[i][-1]:
        print(-1)
    else:
        #动态规划不断加入元素
        r=1
        flag=0
        summ=sum(a[i][:r])
        while not flag:#从前往后太慢了？
            r+=1
            summ+=a[i][r-1]#不要每次都调用sum
            if summ>a[i][r]:
                flag=1
                print(sum(a[i][:r+1]))
