n, m = map(int, input().split())

a = [input() for _ in range(n)]

def lian(a1,a2):
    A1=a1+a1
    A2=a2+a2

    i=0
    j=0

    Lenn=[0]
    for i in range(len(a1)):
        for j in range(len(a2)):
            if A1[i]==A2[j]:
                l1=i
                l2=j
                summ=1
                
                while l1+summ<len(A1) and l2+summ<len(A2):
                    if A1[l1+summ]==A2[l2+summ]:
                        summ+=1
                    else:
                        break
                r1=i+summ-1
                r2=j+summ-1
                

                if r1>len(a1)-1:
                    len1=len(a1)-l1
                else:
                    len1=r1-l1+1
                if r2>len(a2)-1:
                    len2=len(a2)-l2
                else:
                    len2=r2-l2+1

                Lenn.append(max(len1,len2))#Lenn存可能公共字符串长度

    return max(Lenn)

# 全排列 + 计算 MaxLen
k = list(range(n))
vis = [0] * n
b = [0] * n
MaxLen = 0

def dfs(step, summ):
    global MaxLen
    
    if step == n:
        # 计算最后一个和第一个的公共长度
        summ += lian(a[b[0]], a[b[-1]])
        MaxLen = max(MaxLen, summ)
        return
    
    for i in range(n):
        if not vis[i]:
            b[step] = k[i]
            vis[i] = 1
            
            if step > 0:  # 计算当前和前一个字符串的公共长度
                new_summ = summ + lian(a[b[step - 1]], a[b[step]])
            else:
                new_summ = summ

            dfs(step + 1, new_summ)
            vis[i] = 0  # 回溯

dfs(0, 0)

print(MaxLen)
