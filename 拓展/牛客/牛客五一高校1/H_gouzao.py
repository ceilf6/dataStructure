n=int(input())
'''
res = ""
for i in range(2 ** n):
    if bin(i).count('1') % 2 == 0:
        res += "0"  # 偶数个 1，抵抗军
    else:
        res += "1"  # 奇数个 1，幕府军
print(res)
'''

'''
def ct(x):
    cnt=0
    while x:
        x&=x-1
        cnt+=1
    return cnt

res=''

for i in range(1 << n):
    if ct(i)%2==1:
        res+='1'
    else:
        res+='0'
print(res)
'''

n = int(input())
res = '0'
for _ in range(n):
    res += ''.join('1' if c == '0' else '0' for c in res)
print(res)
