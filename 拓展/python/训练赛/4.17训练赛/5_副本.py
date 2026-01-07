l=list(map(int,input().split()))

while 1:
    #try:
    t=int(input())
    if t<0 or t>23:
        break
    m=l[t]
    if m>50:
        print(m,end=' ')
        print('YES')
    else:
        print(m,end=' ')
        print('NO')
    '''
    except:
        break
    '''
