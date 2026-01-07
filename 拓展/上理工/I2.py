x1 = int(input())
y1 = []

for z1 in range(x1):
    a2, b2 = map(int, input().split())
    c2 = input()

    d2 = b2
    e2 = [False] * d2
    f2 = [10**9] * d2
    g2 = [-10**9] * d2
    h2 = [0] * d2
    i2 = list(c2)

    for j2 in range(a2):
        if c2[j2] != '?':
            k2 = c2[j2]
            l2 = ord(k2) - ord('a')
            if 0 <= l2 < d2:
                if not e2[l2]:
                    e2[l2] = True
                    f2[l2] = j2
                    g2[l2] = j2
                    h2[l2] = 0
                else:
                    m2 = min(f2[l2], j2)
                    n2 = max(g2[l2], j2)
                    o2 = n2 - m2
                    p2 = o2 - h2[l2]
                    h2[l2] = o2
                    f2[l2] = m2
                    g2[l2] = n2

    for q2 in range(a2):
        if i2[q2] == '?':
            r2 = 10**18
            s2 = -1
            for t2 in range(d2):
                if not e2[t2]:
                    u2 = 0
                else:
                    v2 = min(f2[t2], q2)
                    w2 = max(g2[t2], q2)
                    x2 = w2 - v2
                    u2 = x2 - h2[t2]
                if u2 < r2 or (u2 == r2 and t2 < s2):
                    r2 = u2
                    s2 = t2
            y2 = s2
            i2[q2] = chr(ord('a') + y2)
            if not e2[y2]:
                e2[y2] = True
                f2[y2] = q2
                g2[y2] = q2
                h2[y2] = 0
            else:
                z2 = min(f2[y2], q2)
                a3 = max(g2[y2], q2)
                b3 = a3 - z2
                h2[y2] = b3
                f2[y2] = z2
                g2[y2] = a3

    c3 = sum(h2)
    y1.append(str(c3))
    y1.append(''.join(i2))

print("\n".join(y1))
