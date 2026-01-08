def shortest_length_after_operations(n, s):
    stack = []
    for char in s:
        if stack and ((stack[-1] == 'f' and char == 'c') or (stack[-1] == 't' and char == 'b')):
            stack.pop()  # 删除符合条件的子串
        else:
            stack.append(char)  # 否则将当前字符入栈
    return len(stack)  # 返回最终栈的大小，即剩余字符的数量

# 输入
n = int(input())  # 字符串长度
s = input()  # 输入字符串

# 输出结果
print(shortest_length_after_operations(n, s))
