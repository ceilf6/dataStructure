from collections import Counter

N = int(input())
s0 = 'CHICKEN'
ls0 = len(s0)

for _ in range(N):
    n = int(input())
    s = list(input())  # 改为列表存储

    p = 0
    q = 0
    flag = 0
    while q < len(s):
        if s[q] == s0[p]:
            p += 1
            del s[q]  # 使用 del 直接删除字符
            q -= 1  # 抵消删除对索引的影响
        if p == ls0:
            flag = 1
            break
        q += 1

    print(s)
    if flag == 0:
        print('NO')
    else:

        count = Counter(s)#统计次数！
        values = sorted(count.values(), reverse=True)



        while 1:
            #  values 为空
            if not values:
                print('YES')
                break #下一例
                
            if len(values)==1:
                print('NO')
                break

                
            values.sort(reverse=True)
            #if len(values) >= 2:
            values[0] -= values[1]
            values.pop(1)#删除索引为1！


                # 过滤掉 0
            values = [v for v in values if v > 0]



