n,m=map(int,input().split())

s=[]
for i in range(n):
    s.append(input())

for i in range(n):
    if 'qiandao' in s[i] or 'easy' in s[i]:
        continue
    else:
        m-=1
        if m==-1:
            print(s[i])

if m>=0:
    print("Wo AK le")
