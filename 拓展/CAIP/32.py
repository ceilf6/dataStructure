n=int(input())
l=list(input().split()) #不用map为int，因为下面也要join

if n==3:
    ans=[[0]*n for i in range(n)]#for _ in range(n-1)]

    #for z in range(n-1):
    for i in range(n):
        for j in range(n):
            ans[i][j]=l[(i+j)%(n)]

    for i in ans:
        #for j in i:
        print(''.join(i))

else:
    vis=[0]*4
    nums=[]
    def dfs(step):
        if step==4:
            nums.append(list(''.join(now)))

        for i in range(4):
            if not vis[i]:
                now[step]=l[i]
                vis[i]=1
                dfs(step+1)
                vis[i]=0
    now=['']*4
    dfs(0)
    m = {d: [0]*4 for d in l}  # 计数表
    result = []
    target_count = 3
    total_required = 4 * 4 * target_count  # 总选中数字数目 = 4位 * 4数字 * 3次 = 48
    
    flag=1
    def backtrack(index, chosen_count):
        global flag
        if flag==0:
            return
        if chosen_count == total_required // 4:  # 选中排列数=48/4=12
            # 输出结果

            for perm in result:
                print(''.join(perm))
            #exit(0)
            flag=0
            return
    
        if index == len(nums):
            return
    
        perm = nums[index]
        # 检查是否可选
        for pos in range(4):
            if m[perm[pos]][pos] == target_count:
                # 超过限制，跳过此排列
                break
        else:
            # 选择该排列
            for pos in range(4):
                m[perm[pos]][pos] += 1
            result.append(perm)
    
            backtrack(index + 1, chosen_count + 1)
    
            # 回溯
            result.pop()
            for pos in range(4):
                m[perm[pos]][pos] -= 1
    
        # 不选该排列，继续
        backtrack(index + 1, chosen_count)
    
    backtrack(0, 0)
