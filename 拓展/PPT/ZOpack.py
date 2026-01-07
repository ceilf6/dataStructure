
def ZOpack(F,c,w):
    for j in range(T,c-1,-1):
        F[j]=max(F[j],F[j-c]+w)


def Cpack(F,c,w):
    for j in range(c,T+1):
        F[j]=max(F[j],F[j-c]+w)


        
T,M=map(int,input().split())

s=[]
for i in range(M):
    s.append(list(map(int,input().split())))

F=[0]*(T+1)

for c,w in s:
    Cpack(F,c,w)

print(F[-1])
