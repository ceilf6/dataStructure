import datetime

s=input()
'''
d=datetime.fromisoformat()

print(d)
'''

'''
s = input("请输入日期（如 2023/04/08）：")
d = datetime.date.strptime(s, "%Y/%m/%d")
print(d)
'''


d = datetime.datetime.strptime(s, "%Y-%m-%d")
print(d.year)   # 输出：2024-04-08

d2 = datetime.date(int(s[:4]),int(s[5:7]),int(s[8:]))
print(d2)
