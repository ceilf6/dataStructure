k = 2024
n = 0

while k > 1:  
    reduced = False  # 标记是否进行了合法操作
    if(k>=20 and k%2==0):
        k//=2
        n+=10
    else:
        for i in range(10, 1, -1):
            if i > 3:
                k2 = k - i
                a = k2 // 100
                b = (k2 // 10) % 10
                c = k2 % 10
            
                if a == i or b == i or c == i:
                    n += 3
                    k -= i
                    reduced = True
                    break  # 进行有效操作后跳出内层循环

        if not reduced:
            k -= 1  
            n += 1

print(n)
