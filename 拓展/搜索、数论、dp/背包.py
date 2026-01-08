def ZOpack(F, c, w):
    for j in range(V, c - 1, -1):
        if F[j - c] + w > F[j]:
            F[j] = F[j - c] + w

def Cpack(F, c, w):
    for j in range(c, V + 1):
        if F[j - c] + w > F[j]:
            F[j] = F[j - c] + w

def Mpack(F, c, w, m):
    if c * m >= V:
        Cpack(F, c, w)
        return
    k = 1
    while k <= m:
        ZOpack(F, c * k, w * k)
        m -= k
        k *= 2
    if m > 0:
        ZOpack(F, c * m, w * m)

n, V = map(int, input().split())
M = []
C = []
W = []
for _ in range(n):
    x, w, v = map(int, input().split())
    M.append(x)
    C.append(w)
    W.append(v)

F = [0] * (V + 1)
for i in range(n):
    Mpack(F, C[i], W[i], M[i])

print(F[-1])
