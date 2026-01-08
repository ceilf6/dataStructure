s=input()

f=input()

def prentx(fs):
    l=len(fs)
    p=[0]*l
    j=0
    for i in range(1,l):
        while j>0 and fs[i]!=fs[j]:
            j=p[j-1]
        if fs[i]==fs[j]:
            j+=1
        p[i]=j
    return p


def KMP(f, s):
    fs = f + '#' + s
    lf = len(f)
    l = len(fs)
    p = [0] * l
    j = 0
    for i in range(1, l):
        while j > 0 and fs[i] != fs[j]:
            j = p[j-1]
        if fs[i] == fs[j]:
            j += 1
        p[i] = j
        # 检查是否匹配且起始位置在分隔符之后
        if p[i] == lf:
            start_in_fs = i - lf + 1  # 匹配在fs中的起始位置
            if start_in_fs > len(f):  # 确保匹配发生在s部分
                return start_in_fs - lf-1  # 转换为s中的下标
    return -1


print(KMP(f,s))
