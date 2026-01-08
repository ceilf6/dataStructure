N=int(input())

n=list(input())

summ=0
s=0
for i in n:
    if i=='(':
        summ+=1
    if i==')':
        s=max(summ,s)
        summ=0

print(s)
