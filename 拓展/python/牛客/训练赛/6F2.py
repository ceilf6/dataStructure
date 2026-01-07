def pan(n):

    if n=='4'or n=='8':
        return 1


    
    # 出现次数
    count = [0] * 10
    for digit in n:
        count[int(digit)] += 1
    
    # 遍历所有可能的
    for num in range(0, 100, 4):
        # 十位和个位
        tens = num // 10
        ones = num % 10
        
        #是否在原始数字出现过
        if count[tens] > 0 and count[ones] > 0:
            if tens == ones:
                if count[tens] >= 2:
                    return 1
            else:
                return 1
    
    return 0

N = int(input())
for _ in range(N):
    n = input()
    if pan(n):
        print('YES')
    else:
        print('NO')
