
n,k=map(int,input().split())
MOD=(10**k)

# 高精度乘法：逐位，可能有进位：自定义函数
# 基于个位的倍数，比如3，那么周期为4，那么cnt+=4

'''
# 补0的不一定不行
if n<MOD//10:
    print(-1)
    exit()
'''

n=str(n%MOD)

n.

kuai=n
m=n
kuai*=(n**2)
kuai%=MOD
m*=n
m%=MOD

cnt=1

while kuai!=m:
    kuai*=(n**2)
    m*=n
    kuai%=MOD
    m%=MOD
    cnt+=1

print(cnt)
