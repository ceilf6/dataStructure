n=int(input())
a=[-1]*n
b=[-1]*n
for i in range(n):
    a[i],b[i]=map(int,input().split())
d=[0]*n
z=n//10
for i in range(n):
    d[i]=a.count(i)-z#出现次数数组，即目标数组
loww=[]
upp=[]
for i in range(n):
    if d[i]>0:
        upp.append(i)
    elif d[i]<0:
        loww.append(i)
upp=sorted(upp,key=lambda x:b[x])
loww=sorted(loww,key=lambda x:b[x])
summ=0
while upp or loww:
    if upp and loww:
        if b[upp[0]]<b[loww[0]]:
            if abs(d[upp[0]])<abs(d[loww[-1]]):
                d[loww[-1]]+=d[upp[0]]

                summ+=abs(d[upp[0]]*b[upp[0]])
                del upp[0]
            elif abs(d[upp[0]])>abs(d[loww[-1]]):
                d[upp[0]]+=d[loww[-1]]
                summ+=abs(d[loww[-1]]*b[upp[0]])
                del loww[-1]
            elif abs(d[upp[0]])==abs(d[loww[-1]]):
                summ+=abs(d[upp[0]]*b[upp[0]])
                del upp[0]
                del loww[-1]
        else:
            if abs(d[loww[0]])<abs(d[upp[-1]]):
                d[upp[-1]]+=d[loww[0]]
                summ+=abs(d[loww[0]]*b[loww[0]])
                del loww[0]
            elif abs(d[loww[0]])>abs(d[upp[-1]]):
                d[loww[0]]+=d[upp[-1]]
                summ+=abs(d[upp[-1]]*b[loww[0]])
                del upp[-1]
            elif abs(d[loww[0]])==abs(d[upp[-1]]):
                summ+=abs(d[loww[0]]*b[loww[0]])
                del loww[0]
                del upp[-1]      
print(summ) 
                

    
