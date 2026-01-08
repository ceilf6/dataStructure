n=int(input())

s=input()

L1=[]
R1=[]
L2=[]
R2=[]


for i in range(n):
    if s[i]=='f':
        L1.append(i)
    if s[i]=='t':
        L2.append(i)
    if s[n-1-i]=='c':
        R1.append(n-1-i)
    if s[n-1-i]=='b':
        R2.append(n-1-i)

l1=len(L1)+len(R1)
l2=len(L2)+len(R2)

while (L1 and R1) or (L2 and R2):
    for i in range(len(L1)):
        for j in range(len(R1)):
            if L1[i]==R1[j]-1:
                del L1[i]
                del R1[j]
                break

    for i in range(len(L2)):
        for j in range(len(R2)):
            if L2[i]==R2[j]-1:
                del L2[i]
                del R2[j]
                break

    print(len(s)-l1-l2+len(L1)+len(R1)+len(L2)+len(R2))
