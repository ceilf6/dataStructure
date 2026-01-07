'''
def main():
    #code here
    t=int(input())
    for _ in range(t):
        a,b=input().split()
        s=-1
        e=-1

        if len(a)!=len(b):
            print('N') #注意特判！
            continue
        for i in range(len(a)):
            if a[i]!=b[i]:
                #print(a,b,i,a[i],b[i])
                s=i
                break
        if s==-1:
            print('Y')
            continue
        
        for j in range(s+1,len(a)):
            if a[j]==b[j]:
                e=j-1 # s到e是不相等的区间
                break

        if e==-1:
            aMid=list(a[s:])
        # split并不能传 '' 空分隔符，而是应该用list
            aMid.reverse()
        # reverse方法并不会返回新数组
            aChange=a[:s]+''.join(aMid)
                                # 在e是不是结尾时得区分处理
        else:
            aMid=list(a[s:e+1])
            aMid.reverse()
            aChange=a[:s]+''.join(aMid)+a[e+1:]

        #print(k1)

        if aChange==b:
            print('Y')
        else:
            print('N')
    pass


if __name__ == '__main__':
    main();
'''

def main():
    t = int(input())
    for _ in range(t):
        a, b = input().split()
        
        if a == b:
            print('Y')
            continue
        
        if len(a) != len(b):
            print('N')
            continue
        
        # 找第一个不相等的位置
        for i in range(len(a)):
            if a[i] != b[i]:
                s = i
                break
        else:
            print('Y')
            continue

        # 应该是找最后一个不相等位置
        for j in range(len(a)-1,i,-1):
            if a[j] != b[j]:
                e = j
                break
        else:
            e = i

        if s!=0:new_a=a[:s]+a[e:s-1:-1]+a[e+1:]
        else:new_a=a[:s]+a[e:s:-1]+a[0]+a[e+1:]
        #print(s,e,new_a)

        if new_a == b:
            print('Y')
        else:
            print('N')

if __name__ == '__main__':
    main()
