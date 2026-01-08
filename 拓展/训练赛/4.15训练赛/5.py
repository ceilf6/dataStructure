n=int(input())
s=[input() for _ in range(n)]
k=int(input())
f=input()

i=0
summ=0
res=''

while i<len(f):
    found=False
    for word in s:
        if f[i:i+len(word)]==word:
            summ+=1
            res+='<censored>'
            i+=len(word)
            found=True
            break
    if not found:
        res+=f[i]
        i+=1

if summ<k:
    print(res)
else:
    print(summ)
    print('He Xie Ni Quan Jia!')
