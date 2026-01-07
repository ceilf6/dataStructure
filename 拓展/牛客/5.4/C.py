n=int(input())
nums=[]

for i in range(n):
    nums.append(input())

from functools import cmp_to_key

# 自定义比较函数
def compare(a, b):
    # 比较 a + b 和 b + a 的字典序
    if a + b < b + a:
        return -1
    elif a + b > b + a:
        return 1
    else:
        return 0


# 排序
sorted_nums = sorted(nums, key=cmp_to_key(compare))

# 拼接结果
result = ''.join(sorted_nums)

# 输出：如果结果有前导零，去掉前导零
print(result)
