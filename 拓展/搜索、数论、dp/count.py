import time
from collections import defaultdict
import bisect
from collections import Counter
import random
for i in (100,1000,10000,100000):
    if i<=1000:print("小规模")
    else:print("中规模")
    n=i
    for j in range(2):
        A=[random.randint(1,n)for _ in range(n)]#A=list(map(int,input().split()))
        A2=A.copy()#A2在二分中用于排序,和A区分开防止影响
        '''
        二分实现count
        '''
        start_time1=time.time()
        l=0
        r=0
        count1={}
        A2.sort()
        while r<len(A2):
            r=bisect.bisect_right(A2,A2[r])
            count1[A2[l]]=r-l
            l=r
        end_time1=time.time()
        print(f"二分count代码用时：{end_time1-start_time1}")

        '''
        系统count
        '''
        start_time2=time.time()
        count2=defaultdict(int)
        for i in A:count2[i]+=1
        end_time2=time.time()
        print(f"系统count代码用时：{end_time2-start_time2}")

        '''
        Counter
        '''
        start_time3=time.time()
        count3=dict(Counter(A))
        end_time3=time.time()
        print(f"Counter用时：{end_time3-start_time3}")


        if (end_time1-start_time1)<(end_time2-start_time2) and (end_time1-start_time1)<(end_time3-start_time3):
            print("二分快")
        elif (end_time2-start_time2)<(end_time1-start_time1) and (end_time2-start_time2)<(end_time3-start_time3):
            print("系统自带的快")
        else:
            print("Counter快")
        print()
