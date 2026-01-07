t = int(input())
for _ in range(t):
    n, m, l, r = map(int, input().split())
    extra_left = min(m, -l) 
    extra_right = m - extra_left  

    l_prime = 0 - extra_left
    r_prime = 0 + extra_right

    print(l_prime, r_prime)
