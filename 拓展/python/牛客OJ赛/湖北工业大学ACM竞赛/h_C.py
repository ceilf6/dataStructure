n=int(input())

nums=[[]for i in range(n)]

for i in range(n):
    nums[i]=list(map(int,input().split()))

for i in range(n):
    d10=abs(nums[i][1]-nums[i][0])
    d20=abs(nums[i][2]-nums[i][0])
    d21=abs(nums[i][2]-nums[i][1])

    if sum(nums[i])==0:
        print('NO')
    elif (d10%3==0 and nums[i][2]>=d10/3) or (d20%3==0 and nums[i][1]>=d20/3) or (d21%3==0 and nums[i][0]>=d21/3):
        print('YES')
    else:
        print('NO')
