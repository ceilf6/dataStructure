s=input()

L=len(s)

if L<=6:
    print('False')
    exit()

flag1=[0,0,0]

flag2=0

for i in s:
    if '1'<=i<='9':
        flag1[2]=1
        if flag2:
            print('False')
            exit()
        flag2=1
    else:
        flag2=0
        if 'a'<=i<='z':
            flag1[0]=1
        elif 'A'<=i<='Z':
            flag1[1]=1
if sum(flag1)==3:
    print('True')
else:
    print('False')
