s=[]

while True:
    temp=input()
    if temp!='':    #直接用''判断是不是空行吧，因为EOF是需要用ctrl来停止
        s+=list(temp.split()) #不是用append，不然列表里面有很多小列表
    else:
        break

'''
while True:
    try:
        s.append(list(input().split()))
    except EOFError:
        #pass
        break
'''
print(s)

#print(ord('A'),ord('Z'),ord('a'),ord('z'),ord('0'),ord('9'))

ans=0

l=0

cnt=0

for i in s:
    k=[0]*3
    for j in i:
        if 65<=ord(j)<=90:
            k[0]=1
        elif 97<=ord(j)<=122:
            k[1]=1
        elif 48<=ord(j)<=57:
            k[2]=1
        if sum(k)==3:
            break

    if sum(k)!=0:
        l+=len(i)
        cnt+=1
        if sum(k)==3:
            ans+=5
        elif (k[0] or k[1]) and k[2]:
            ans+=3
        elif k[0] and k[1]:
            ans+=1
        

print(ans)
print(l,cnt)
