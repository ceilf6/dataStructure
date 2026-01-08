#不需要 from copy import copy #比赛能用吗

n=int(input())
l=len(str(n))
n2=[int(d) for d in str(n)] #转化整数为可索引的数组

dp=[[0]*l for _ in range(l)]

an1=0

def ch(i,j):
    cn2=n2.copy()
    for k in range((j-i)//2+1):
        cn2[i+k],cn2[j-k]=cn2[j-k],cn2[i+k]
    return ch2(cn2)

def ch2(k):
    n3=int(''.join(map(str,k))) #转化数组为整数
    return n3

def yi_ban():
    global an1
    for i in range(0,l-1):
        for j in range(i,l-1):
            if ch(i,j)<n:
                an1+=1

def dp(i,j):
    dp[i][j]=dp[i]





yi_ban()
print(an1)
