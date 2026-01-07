s=input()

L=len(s)

l=0
r=0

def checktype(k):
    if '0'<=k<='9':
        return 0
    else:
        return 1

ans=''

# 轮转：26进制！

while r<L:
    if checktype(s[l])!=checktype(s[r]):

        if checktype(s[l])==1:
            cnt=0
            for i in range(r-1,l-1,-1):
                cnt+=26**(r-i-1)*(ord(s[i])-97)

            ans+=str(cnt)
        else:
            add=''
            cnt=int(s[l:r])
            while cnt:
                add+=chr(cnt%26+97)
                cnt//=26
            ans+=add[::-1]
        l=r
    else:
        if r==l:
            if s[l]=='0':
                ans+='a'
                l+=1
            elif s[l]=='a':
                ans+='0'
                l+=1

    r+=1

if checktype(s[l])==1:
    cnt=0
    for i in range(r-1,l-1,-1):
        cnt+=26**(r-i-1)*(ord(s[i])-97)
    ans+=str(cnt)
else:
    add=''
    cnt=int(s[l:r])
    while cnt:
        add+=chr(cnt%26+97)
        cnt//=26
    ans+=add[::-1]
print(ans)
