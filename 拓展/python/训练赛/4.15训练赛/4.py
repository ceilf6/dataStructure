# 输入人数和技能数
n, m = map(int, input().split())
# 输入每项技能的人数
skills = list(map(int, input().split()))

# 所有技能点的总和
total_skill_points = sum(skills)

# 假设每个人最多会 m-1 项技能，最多产生的技能点是 n*(m-1)
# 如果总技能点超过这个值，那么至少有 (total - n*(m-1)) 人必须全部都会
min_all_skills = total_skill_points - n * (m - 1)

# 最少会 m 项技能的人不能小于 0
print(max(min_all_skills, 0))
