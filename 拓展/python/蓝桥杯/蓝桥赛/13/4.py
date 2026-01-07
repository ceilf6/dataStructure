
T=int(input())
for i in range(T):
    a1,a2,b1,b2,c1,c2=map(int,input().split())

    arr=[
        [a1,a2],
        [b1,b2],
        [c1,c2]
        ]

    ans=100
    if arr[0][0]==arr[1][0]+arr[2][0]:
        if arr[1][1]==arr[2][1]:
            print(4)
            continue
        else:
            ans=min(ans,6)
    elif arr[0][0]==arr[1][1]+arr[2][0]:
        if arr[1][1]==arr[2][1]:
            print(4)
            continue
        else:
            ans=min(ans,6)
    elif arr[0][1]==arr[1][0]+arr[2][0]:
        if arr[1][1]==arr[2][1]:
            print(4)
            continue
        else:
            ans=min(ans,6)
    elif arr[1][0]==arr[0][0]+arr[2][0]:
        if arr[0][1]==arr[2][1]:
            print(4)
            continue
        else:
            ans=min(ans,6)
