# 更复杂的测试用例
test_input2 = """1
5
1 10 1 5
1 2 5
2 3 2
2 4 8
4 5 3
"""

with open('/Users/a86198/Desktop/未命名文件夹/test_input2.txt', 'w') as f:
    f.write(test_input2)

print("第二个测试输入已创建")
print("树结构：")
print("1 -- 2 -- 3")
print("     |")
print("     4 -- 5")
print("边权：1-2(5), 2-3(2), 2-4(8), 4-5(3)")
print("体力增益：节点2(1), 节点3(10), 节点4(1), 节点5(5)")
