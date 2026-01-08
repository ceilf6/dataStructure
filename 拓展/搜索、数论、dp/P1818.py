def count_i(s):
    nums=list(map(int,s))
    inv_c=0
    n=len(s)
    for i in range(n):
        for j in range(i+1,n):
            if nums[i]>nums[j]:
                inv_c+=1
    return inv_c

s1='123456789'
T=int(input())

for i in range(T):
    mapp=[[] for i in range(3)]
    for i in range(3):
        mapp[i]=list(map(int,input().split()))
    s2=''.join(''.join(map(str,x)) for x in mapp)
    
    print(s2)
    if count_i(s1)%2!=count_i(s2)%2:
        print(-1)
        continue
