T=int(input())

s=['']*T

for i in range(T):
    n=int(input())
    s[i]=input()

for i in range(T):
    a=s[i]
    a_last=''
    flag=1
    while flag:
        a=a.replace('11','')
        a=a.replace('00','')
        if a_last==a:
            flag=0
        a_last=a
    if a:
        if a[0]=='1':
            print(a.count('0'))
        else:
            print(a.count('1'))
    else:
        print(0)
    
    
'''
for i in range(T):
    a=s[i]
    j=1
    while 1<=j<len(a):
        if a[j]==a[j-1]:
            a=a[:j-1]+a[j+1:]
            #print(a,j)
            j-=2
            #print(j)
        if j==-1:
            j+=2
        else:
            j+=1
        #print(j)

    #print(a)
    if a:
        if a[0]=='1':
            print(a.count('0'))
        else:
            print(a.count('1'))
    else:
        print(0)
'''
'''
for i in range(T):
    a=s[i]
    summ1=0
    summ0=0
    n1=a.count('1')
    n0=a.count('0')
    j=0
    while j<len(a):
        if a[j]==a[j-1]=='1':
            j+=1
            summ1+=2
        elif a[j]==a[j-1]=='0':
            j+=1
            summ0+=2
        j+=1

    if n1-summ1<n0-summ0:
        print(n1-summ1)
    else:
        print(n0-summ0)
'''
