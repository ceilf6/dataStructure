n, m = map(int, input().split())
# 使用集合存储每个物品的拥有者
items_owners = [set() for _ in range(m + 1)]

for person in range(1, n + 1):
    data = list(map(int, input().split()))
    k = data[0]
    items = data[1:]
    for item in items:
        items_owners[item].add(person)

q = int(input())
for _ in range(q):
    a, b = map(int, input().split())
    # 计算两个集合的交集的大小
    print(len(items_owners[a] & items_owners[b]))
