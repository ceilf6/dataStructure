# 请在此输入您的代码
n, x = input().split()
n = int(n)
x = int(x)

str_list = sorted(input())

# print(str_list)

last = str_list[x - 1]
print(str_list)
if last != str_list[0]:
  print(last)
elif str_list[x] == str_list[-1]:
  for i in range(0,len(str_list),x):
    print(str_list[i],end='')
else:
    print(''.join(str_list[x-1:]))
