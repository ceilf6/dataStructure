


kua=[]

n,m,ll=map(int,input().split())

s=[[]]
for i in range(n):
    s.append(list(input()))
#print(s)
l=list(map(int,input().split()))

for i in range(len(l)-1):
    if l[i]==0:
        if kua:
            out=kua[-1]
            del kua[-1]
            print(out,end='')
            #print(kua)
    else:

        if len(kua)==ll:
            print(kua[-1],end='')
            del kua[-1]

        if s[l[i]]:
            inn=s[l[i]][0]
            del s[l[i]][0]
            kua.append(inn)
            



        
