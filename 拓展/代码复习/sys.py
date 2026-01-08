import sys

try:
    # 尝试设置一个极大的值（如 sys.maxsize）
    sys.setrecursionlimit(1000000)
    print(sys.maxsize-1)
    print("设置成功")
except OverflowError:
    print("数值超出 C long 范围，触发 OverflowError")
