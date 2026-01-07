n,c=map(int,input().split())
name=['']*n
num=[[i,0]for i in range(n)]
for i in range(n):
    name[i],nn=input().split()
    num[i][1]=int(nn)
room=[]
contact=[[]for _ in range(n)]
while any(x[1]>0 for x in num):
    num=sorted(num,key=lambda x:x[1],reverse=1)
    sid=num[0][0]
    cnt=num[0][1]
    if cnt>=c:
        room.append([c-c,sid])
        contact[sid].append(len(room)-1)
        num[0][1]-=c
    else:
        flag=0
        for i in range(len(room)):
            if room[i][0]>=cnt:
                room[i][0]-=cnt
                contact[sid].append(i)
                num[0][1]=0
                flag=1
                break
        if not flag:
            room.append([c-cnt,sid])
            contact[sid].append(len(room)-1)
            num[0][1]=0
for i in range(n):
    print(name[i],len(set(contact[i])))
print(len(room))
