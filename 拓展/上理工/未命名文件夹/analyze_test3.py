# 分析第三个测试用例
test_case_3 = """1
7
3 2 6 8 2 1
1 2 4
1 4 7
3 2 5
7 6 6
6 4 9
4 5 1
"""

with open('/Users/a86198/Desktop/未命名文件夹/test3.txt', 'w') as f:
    f.write(test_case_3)

print("第三个测试用例：")
print("节点数: 7")
print("体力增益: 节点2(3), 节点3(2), 节点4(6), 节点5(8), 节点6(2), 节点7(1)")
print("边:")
print("1-2 (权重4)")
print("1-4 (权重7)")  
print("3-2 (权重5)")
print("7-6 (权重6)")
print("6-4 (权重9)")
print("4-5 (权重1)")
print()
print("理想输出: 4 6 7 7 7 7")
print("我的输出: 4 6 7 7 10 14")
print()
print("问题出现在节点6和7")
