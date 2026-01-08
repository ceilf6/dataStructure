n=int(input("输入总共有几张牌"))
sum=0
nn=0 #抓取次数
k=0
while sum<n:
    nn+=1
    k+=1
    sum+=3**k
#结束的时候，最后一次谁抓就是谁
if (nn-1)//2==1:
    print("Bob")
else:
    print("Alice")#输出的是获胜的人