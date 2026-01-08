n = int(input())
s = input()

L1 = []
R1 = []
L2 = []
R2 = []

for i in range(n):
    if s[i] == 'f':
        L1.append(i)
    if s[i] == 't':
        L2.append(i)
    if s[n-1-i] == 'c':
        R1.append(n-1-i)
    if s[n-1-i] == 'b':
        R2.append(n-1-i)

l1 = len(L1) + len(R1)
l2 = len(L2) + len(R2)

while (L1 and R1) or (L2 and R2):
    to_remove_L1 = []
    to_remove_R1 = []
    to_remove_L2 = []
    to_remove_R2 = []

    for i in range(len(L1)):
        for j in range(len(R1)):
            if L1[i] == R1[j] - 1:
                to_remove_L1.append(i)
                to_remove_R1.append(j)
                break

    for i in range(len(L2)):
        for j in range(len(R2)):
            if L2[i] == R2[j] - 1:
                to_remove_L2.append(i)
                to_remove_R2.append(j)
                break

    # 先删除所有匹配的元素
    for i in reversed(to_remove_L1):
        del L1[i]
    for j in reversed(to_remove_R1):
        del R1[j]
    for i in reversed(to_remove_L2):
        del L2[i]
    for j in reversed(to_remove_R2):
        del R2[j]

    print(len(s) - l1 - l2 + len(L1) + len(R1) + len(L2) + len(R2))
