'''
💡题目描述（中文翻译）

你得到一个长度为 N 的字符串 S，只由以下三种字符组成：
	•	.：表示空位
	•	o：表示确定放置了“o”
	•	?：表示待确定，可以替换成.或o

你可以把字符串 S 中的每一个 ? 独立地替换成 . 或 o，从而构造出很多不同的字符串。

在这些所有构造出来的字符串中，设 X 是其中满足下面所有条件的字符串集合：
	1.	字符 o 的数量恰好是 K 个；
	2.	任意两个 o 不能相邻（也就是说不能出现 “oo”）；
	3.	保证集合 X 非空（即至少存在一种替换方案，使上述条件成立）；

⸻

现在你要构造一个新字符串 T，满足：
	•	对于每一个位置 i（1 ≤ i ≤ N）：
	•	如果在 所有的字符串 X 中，第 i 个字符一定是 .，那么 T 的第 i 个字符也为 .；
	•	如果在 所有的字符串 X 中，第 i 个字符一定是 o，那么 T 的第 i 个字符也为 o；
	•	如果在 字符串 X 中有的第 i 位是 .，有的第 i 位是 o，那么 T 的第 i 个字符为 ?。
'''

n,k=map(int,input().split())

s=input()

ans=[]
def dfs(step,b,no,numo):
    if step==n:
        if numo==k:
            ans.append(''.join(b))
        return

    b2=b.copy()
    if s[step]=='o':
        if no:
            return
        else:
            if numo<k:
                b2.append('o')
                dfs(step+1,b2,1,numo+1)

    elif s[step]=='.':
        b2.append('.')
        dfs(step+1,b2,0,numo)
    else:
        if no:
            b2.append('.')
            dfs(step+1,b2,0,numo)
        else:
            b3=b.copy()
            b3.append('.')
            dfs(step+1,b3,0,numo)
            if numo<k:
                b2.append('o')
                dfs(step+1,b2,no+1,numo+1)



dfs(0,[],0,0)
x=''
for i in range(n):
    flag1=0
    flag2=0
    for j in ans:
        if flag1 and flag2:
            break
        if j[i]=='o':
            flag1=1
        elif j[i]=='.':
            flag2=1
    if flag1 and flag2:
        x=x+'?'
    elif flag1:
        x=x+'o'
    else:
        x=x+'.'

print(x)
        
    
