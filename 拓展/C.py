import sys
input = sys.stdin.readline

MOD = 10**9 + 7
BASE = 131

n, q = map(int, input().split())
s = input().strip()
S = list(s)

# 滚动哈希预处理
def build_hash(s):
    n = len(s)
    H = [0] * (n + 1)
    P = [1] * (n + 1)
    for i in range(1, n + 1):
        H[i] = (H[i-1] * BASE + ord(s[i-1])) % MOD
        P[i] = P[i-1] * BASE % MOD
    return H, P

def get_hash(H, P, l, r):  # s[l:r] 的哈希（下标从0开始）
    return (H[r] - H[l] * P[r - l]) % MOD

# KMP前缀函数（构造 border）
def get_borders(s):
    n = len(s)
    pi = [0] * n
    for i in range(1, n):
        j = pi[i-1]
        while j and s[i] != s[j]:
            j = pi[j-1]
        if s[i] == s[j]:
            j += 1
        pi[i] = j
    borders = []
    k = n
    while k:
        borders.append(k)
        k = pi[k-1]
    return borders

for _ in range(q):
    op = input()
    if op[0] == '1':
        _, ch = op.strip().split()
        S.append(ch)
    else:
        _, k = op.strip().split()
        k = int(k)
        cur = ''.join(S)
        n = len(cur)

        H, P = build_hash(cur)

        borders = get_borders(cur)
        borders.sort(reverse=True)

        found = -1
        for l in borders:
            h = get_hash(H, P, 0, l)  # 当前候选串的哈希值
            cnt = 0
            for i in range(n - l + 1):
                if get_hash(H, P, i, i + l) == h:
                    cnt += 1
                    if cnt >= k:
                        found = l
                        break
            if found != -1:
                break
        print(found)










#----------------------------


n,q=map(int,input().split())

s=input()
#s2=s[::-1]
l=len(s)
from functools import cache

@cache
def count(now,ln):
    cnt=0
    for i in range(l):
        if s[i:i+ln]==now:
            cnt+=1
            if cnt>=k:
                return 1
    return 0


for _ in range(q):
    a,k=input().split()

    if a=='1':
        s+=k
        #s2=k+s2
        l+=1
        continue
        #print(s)

    k=int(k)
    flag=0
    for i in range(l-k+1,0,-1):
        if s[:i]==s[l-i:]:
            now=s[:i]
            
            print(now)

            if count(now,i):
                print(i)
                flag=1
                break

    if(not flag):print(-1)
