class Solution:
    def solveNQueens(self, n):

        ans=[]
        #vis=[0]*(2*n-1)    #set() #保存已经访问的行/列/斜（斜向1:行号加列号是不变的；斜向2:行号减列号相同）
        vis1=set()
        vis2=set()
        vis3=set()
        vis4=set()

        b=[]    #每次当前的选择，也可以用dfs中传入，但是会占用更多空间
        def dfs(step):
            if step==n:
                l=['.'*n for _ in range(n)]
                print(l)
                for i in b:
                    print(i)
                    l[i[0]]=l[i[0]][:i[1]]+'Q'+l[i[0]][i[1]+1:]
                ans.append(l)
                return  #别忘记终止

            for i in range(n):
                if i in vis1:#同行
                    continue
                for j in range(n):
                    if j in vis2:#同列
                        continue
                    if i+j in vis3:#同斜1
                        continue
                    d=abs(i-j)
                    if d in vis4:#同斜2
                        continue

                    b.append([i,j])

                    vis1.add(i)
                    vis2.add(j)
                    vis3.add(i+j)
                    vis4.add(d)

                    dfs(step+1)
                    
                    b.pop()
                    vis1.remove(i)
                    vis2.remove(j)
                    vis3.remove(i+j)
                    vis4.remove(d)
                    #恢复现场，方便后面分支探索
        dfs(0)
        
        return ans

if __name__=='__main__':
    n=4

    sol=Solution()
    ans=sol.solveNQueens(n)
    print(ans)
