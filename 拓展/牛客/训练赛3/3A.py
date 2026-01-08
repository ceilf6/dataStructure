l=list(map(int,input().split()))

l.sort()

l1=[l[0]*2,l[1],l[2]]

l2=[l[0],l[1]*2,l[2]]

l1.sort()

l2.sort()

if l1[0]+l1[1]>l1[2] or l2[0]+l2[1]>l2[2]:
    print('Yes')
else:
    print('No')
