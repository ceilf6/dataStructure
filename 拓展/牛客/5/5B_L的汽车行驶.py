s=0
v=0

def c0():
    global v,s
    v+=10
    s+=v

def c1():
    global v,s
    if v>=5:
        v-=5
    else:
        v=0
    s+=v

def c2():
    global v,s
    v0=v
    if v>=10:
        v-=10
    else:
        v=0
    s+=v
    v=v0

n=int(input())

C=list(map(int,input()))

for i in C:
    if i==0:
        c0()
    elif i==1:
        c1()
    else:
        c2()

print(s)
    
