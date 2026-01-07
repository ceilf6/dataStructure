T=int(input())

def fenzhi(s,l):
    if l==2:
        return s[0]

    mid=l//2

    left=fenzhi(s[:mid],mid)
    r=fenzhi(s[mid:],mid)

    if l!=8:
        return left

    else:
        if left==r:return left
        else:
            nl=s.count(left)
            nr=s.count(r)
            if nl>nr:
                return left
            elif nl<nr:
                return r
            else:
                return 'N'

for _ in range(T):
    s=input()
    print(fenzhi(s,8))
