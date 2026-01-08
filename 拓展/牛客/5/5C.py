n,x,y=map(int,input().split())
a=input()
b=input()
c=input()

b2=int(a,2)^int(c,2)#异或是把该数转为二进制再运算，现在我就是二进制
        #int函数：str用k进制转化

b2 = bin(b2)[2:].zfill(n)[-n:]  # 保证输出 n 位
    #输出str类型

def fd(b1: str, b2: str) -> str:
    # 计算异或结果，1 表示不同位
    diff_mask = int(b1, 2) ^ int(b2, 2)
    # 用掩码提取 b1 中不同部分
    result = ''.join(b1[i] if (diff_mask >> (len(b1) - 1 - i)) & 1 else '' for i in range(len(b1)))
    return result

bd=fd(b,b2)

sum0=0
sum1=0

for i in bd:
    if i=='0':
        sum0+=1
    elif i=='1':
        sum1+=1

if y>2*x:
    print(len(bd)*x)
else:
    maxx=max(sum0,sum1)
    minn=min(sum0,sum1)
    print(minn*y+(maxx-minn)*x)
