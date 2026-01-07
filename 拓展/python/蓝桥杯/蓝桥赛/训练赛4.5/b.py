import re

text = "This is a story about Alice and Bob. Alice wants to send a private message to Bob."
matches = [m.start() for m in re.finditer("Bob", text)]
print(matches)  # 输出：[27, 76]，表示 Bob 出现的位置
