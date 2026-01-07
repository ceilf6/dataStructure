
import bisect as bi

N=int(input())

b=list(map(int,input().split()))

a=list(map(int,input().split()))

b.sort()

#print(a,b)

a2=[]
summ=0
#dang=0
for i in range(len(b)):
    bi.insort(a2,a[i])
    #print(a2)

    summ+=bi.bisect_left(a2,b[i])
    
    '''
    J=0
    for j in range(len(a2)):
        if a[i]<a2[j]:
            J=j
            break
        if j==len(a2)-1:
            J=len(a2)
    a2=a2[:J]+[a[i]]+a2[J:]
    #print(a2)
    '''

    '''
    a2.append(a[i])
    a2.sort(reverse=0)
    '''
    '''
    #print(a2,i)
    dang=0
    #print(a2)
    for j in range(0,len(a2)):
        
        if b[i]>a2[j]:
            dang+=1
        else:
            #print(dang)
            summ+=dang
            break
        if j==(len(a2)-1):
            summ+=dang
            '''
print(summ)



'''
summ=0
for i in range(len(b)):
    for j in range(i+1):
        if b[i]>a[j]:
            summ+=1
'''
'''转移方程错误
#dp=[b[0]>a[0]]
I=0
flag=0
for i in range(len(b)):
    if flag:
        break
    for j in range(i+1):
        if b[i]>a[j]:
            I=i
            #print(i)
            flag=1
            break
#print(I)
summ=[0]*N
summ[I]=1
#print(dp)
for i in range(I+1,len(a)):
    summ[i]=summ[i-1]+(b[i]>a[i])

'''
