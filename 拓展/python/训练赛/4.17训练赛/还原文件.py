from collections import deque

class AhoCorasick:
    def __init__(self):
        self.tree = [{}]  # Trie树
        self.fail = [-1]  # 失败指针
        self.output = [{}]  # 匹配的模式串结果

    def add_word(self, word, index):
        """将模式串添加到AC自动机"""
        node = 0
        for char in word:
            if char not in self.tree[node]:
                self.tree[node][char] = len(self.tree)
                self.tree.append({})
                self.fail.append(-1)
                self.output.append({})
            node = self.tree[node][char]
        self.output[node][index] = True  # 记录匹配到的模式串的索引

    def build(self):
        """构建失败指针"""
        queue = deque()
        for char in range(256):
            if chr(char) in self.tree[0]:
                node = self.tree[0][chr(char)]
                self.fail[node] = 0
                queue.append(node)
            else:
                self.tree[0][chr(char)] = 0  # 没有这个字符，指向根节点

        # BFS构建失败指针
        while queue:
            r = queue.popleft()
            for char, u in self.tree[r].items():
                queue.append(u)
                state = self.fail[r]
                while char not in self.tree[state]:
                    state = self.fail[state]
                self.fail[u] = self.tree[state][char]
                self.output[u].update(self.output[self.fail[u]])

    def search(self, text):
        """在文本中查找所有匹配的模式串"""
        node = 0
        result = []
        for i in range(len(text)):
            char = text[i]
            while char not in self.tree[node]:
                node = self.fail[node]
            node = self.tree[node][char]
            if self.output[node]:
                for index in self.output[node]:
                    result.append((i, index))  # 匹配到的模式串的结束位置和索引
        return result


# 输入处理
N = int(input())  # 半张纸的角点数
half_paper = list(map(int, input().split()))  # 半张纸的断口折线

M = int(input())  # 碎纸机里的纸条数
paper_fragments = []
for _ in range(M):
    fragment = list(map(int, input().split()))
    paper_fragments.append(fragment[1:])  # 取每个碎片的高度值

# 构建AC自动机
ac = AhoCorasick()
for i, fragment in enumerate(paper_fragments):
    ac.add_word(fragment, i + 1)  # 添加每个碎片

ac.build()

# 在半张纸的折线中查找匹配的顺序
result = []
for fragment in paper_fragments:
    matches = ac.search(half_paper)
    for match in matches:
        result.append(match[1])

# 输出最终拼接的顺序
print(" ".join(map(str, result)))
