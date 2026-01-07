class segTree:
    def __init__(self,n,arr=None): #py必须将self显式地写在第一个
        self.n=     n          # 线段树大小
        self.tree=  []*( 4*n ) # 开一个4n大的数组存储查询目标值
        self.lazy_= []*( 4*n ) #                     懒标记

        if arr is not None:
            self.arr=[0]+arr #根节点编号从1开始
            self.build(1,1,n)


    def build(self,node,l,r):
        if l==r:
            # 叶子节点：直接赋值
            self.tree[node]=self.arr[l]
        else:
            # 分治赋值
            mid=(l+r)//2
            self.build(node*2  ,l    ,mid)
            self.build(node*2+1,mid+1,r  )
            #向上维护
            self.tree[node]=self.tree[node*2]+self.tree[node*2+1]


    def push(self,node,l,r):
        mid=(l+r)//2
        #分治
        ''' 注意懒标记处理优先级 '''
        if self.lazy_[node] is not None: # 必须用is not None，因为假值 0 也是有效赋值
            val=self.lazy_[node]
            #处理值
            self.tree[node*2]       #左子树：mid-l+1
            self.tree[node*2+1]     #右子树：r-mid
            #下放懒标记
            self.lazy_[node*2]
            self.lazy_[node*2+1]
            ''' 可能会对其他懒标记产生影响 '''
            #清除当前节点懒标记
            self.lazy_[node]


    def update_(self,node,l,r,ql,qr,val): # 对于不同的操作进行更新目标值
        # 1.完全覆盖：直接在当前节点打懒标记，不需要继续递归
        if ql<=l and qr>=r:
            self.tree[node]
            # 有时候根据优先级需要进行分支判断更新标记
            self.lazy_[node]
            
        else:
        # 2.部分覆盖：需要继续递归，所以 2.1先调用push初始化
            self.push(node,l,r)
            mid=(l+r)//2
            if ql<=mid: # 2.2通过判断确定更新方向
                self.update_    # node*2  ,l    ,mid,ql,qr,val
            if qr>mid:
                self.update_    # node*2+1,mid+1,r  ,ql,qr,val
            # 2.3向上维护：更新当前节点的值（一般求和就是直接+）
            self.tree[node]=self.tree[node*2]+self.tree[node*2+1]


    def query(self,node,l,r,ql,qr): # 查询目标值
        # 1.完全覆盖：直接返回当前节点值
        if ql<=l and qr>=r:
            return self.tree[node]
        else:
        # 2.部分覆盖：
            self.push(node,l,r) # 2.1还是先调用push初始化
            mid=(l+r)//2
            res=0
            if ql<=mid:
                res+=self.query(node*2, l     ,mid,ql,qr,val)
            if qr>mid:
                res+=self.query(node*2+1,mid+1,r  ,ql,qr,val)
            return res


def solve():
    n=
    Tree=segTree(n)

    '''
    Tree.update( 1 , 1 , n , l , r , val )
             #根节点          输入范围 输入的更新值
    '''


if __name__=='__main__':
    solve()
