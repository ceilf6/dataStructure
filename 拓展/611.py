class Solution:
    from sortedcontainers import SortedSet
    def triangleNumber(self, nums: List[int]) -> int:
        nums=SortedSet(nums)
        ln=len(nums)
        ans=0
        for i in range(ln-2):#枚举第一个，要给后面两个留位置
            for j in range(i+1,ln-1):
                l=nums[j]-nums[i]#abs(nums[i]-nums[j])
                r=nums[j]+nums[i]
                print(nums.irange(l+1,r-1))
        return ans

if __name__=='__main__':
    nums=[4,2,3,4]
    sol=Solution()
    ans=sol.triangleNumber(nums)
    print(ans)
