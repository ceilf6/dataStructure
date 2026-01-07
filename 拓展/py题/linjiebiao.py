inn=[]
for i in range(3):
    inn.append(list(map(int,input().split())))
'''
while 1:
    try:
        inn.append(list(map(int,input().split())))
    except l==[-1]:#EOFError:
        break
'''
#3.邻接表
from collections import defaultdict
d=defaultdict(list)
for a,b,k in inn:#inn是输入内容
    d[a].append((b,k))

for i in d:
    print(d[i])
