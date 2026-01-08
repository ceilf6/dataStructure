T=int(input())
for i in range(T):
    n=int(input())
    s=input()

    n1=s.count('1')
    n2=s.count('0')

    summ=n1-n2

    '''
    if summ<=0:
        print(0)
    '''

    k1=(summ+1)//2
    k2=summ//2
    print(k1*k2)
    '''
    else:
        k1=(summ-1)//2
        k2=summ//2
        print(k1*k2)
    '''

import sys

T=int(input())
for i in range(T):
    n=int(input())
    s=input()

    total_ones = s.count('1')
    total_zeros = n - total_ones
    total_cute = total_ones - total_zeros

    left_ones = 0
    left_zeros = 0
    max_product = float('-inf')

    for i in range(n - 1):
        if s[i] == '1':
            left_ones += 1
        else:
            left_zeros += 1

        left_cute = left_ones - left_zeros
        right_cute = total_cute - left_cute
        max_product = max(max_product, left_cute * right_cute)

    print(max_product)
