'''
while True:
    temp=input()
    if temp!='':    #直接用''判断是不是空行吧，因为EOF是需要用ctrl来停止
        s+=''.join(list(temp.split())) #不是用append，不然列表里面有很多小列表
    else:
        break
'''

#换行符也是分割符号，所以最好是一行行处理

ans=0
L=0
cnt=0

while True:
    try:
        s=input()
    except EOFError:
        break
    
    if s=='':
        a=1
        #break
    else:
        l=0
        r=0
        k=[0]*3
        while r<len(s): #右拖左式双指针
            if 65<=ord(s[r])<=90:
                k[0]=1
            elif 97<=ord(s[r])<=122:
                k[1]=1
            elif 48<=ord(s[r])<=57:
                k[2]=1
            else:
                if sum(k)!=0:
                    L+=r-l
                    cnt+=1
                    if sum(k)==3:
                        ans+=5
                    elif (k[0] or k[1]) and k[2]:
                        ans+=3
                    elif k[0] and k[1]:
                        ans+=1
                l=r+1
                k=[0]*3

            r+=1 #别忘记往后走

        # 别忘记处理最后一段
        if sum(k)!=0:
            L+=r-l
            cnt+=1
            if sum(k)==3:
                ans+=5
            elif (k[0] or k[1]) and k[2]:
                ans+=3
            elif k[0] and k[1]:
                ans+=1


print(ans)
print(L,cnt)
