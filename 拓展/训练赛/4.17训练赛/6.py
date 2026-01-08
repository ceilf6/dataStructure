
f1=input()
f2=input()

def cz(f):
    ans=''
    for i in range(1,len(f)):
        if int(f[i])%2==int(f[i-1])%2:
            ans+=max(f[i],f[i-1])

    return ans

s1=cz(f1)
s2=cz(f2)

if s1==s2:
    print(s1)
else:
    print(s1)
    print(s2)
