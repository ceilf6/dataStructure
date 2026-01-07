
def solve_I(n, m, s):
    from collections import defaultdict
    cnt = defaultdict(int)
    pos = defaultdict(list)
    for i, c in enumerate(s):
        cnt[c] += 1
        pos[c].append(i)

    high = [c for c in sorted(cnt) if cnt[c] >= 2]
    # 初始化结果
    res = ['?'] * n

    # 1. 填充高频字符间隙
    for c in high:
        pp = pos[c]
        for i in range(len(pp) - 1):
            l, r = pp[i], pp[i + 1]
            for k in range(l + 1, r):
                if res[k] == '?':
                    res[k] = c

    # 2. 收集剩余槽
    empties = [i for i in range(n) if res[i] == '?']

    # 3. 剩余字符（包括cnt==1和cnt==0），选前 m 个
    rem_chars = [c for c in sorted({chr(ord('a') + i) for i in range(m)}) if cnt[c] < 2]
    rem_chars = rem_chars[:m]  # 取前m个

    # 平均分配
    T = len(rem_chars)
    for idx, posi in enumerate(empties):
        res[posi] = rem_chars[idx % T]

    return "".join(res)


T=int(input())

for _ in range(T):
    
    n,m=map(int,input().split())
    s=input()
    ls=len(s)


    print(solve_I(n,m,s))
    '''
    l=0
    r=ls-1

    while l<r:
        ch=s[l]
        if ch!='?':
            for i in range(r,l,-1):
                if s[i]==ch:
                    #for j in range(l+1,i):
                    s=s[:l+1]+ch*(i-l-1)+s[i:]
                    l=i+1
                    r=ls-1
                    break
    '''
    

    
