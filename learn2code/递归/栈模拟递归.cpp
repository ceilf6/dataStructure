/*
在实际过程中如果遇到复杂问题 DFS 会爆栈
那么可以用 栈 模拟实现递归，栈中需要存储所有上下文信息
- 参数
- 局部变量
- 返回位置

阶段数 = 递归调用次数+1（即DFS中DFS出现次数+1）
*/

#include <string>
#include <iostream>
#include <stack>

// 栈帧：模拟递归调用时的上下文
struct Frame
{
    int step;          // 参数：要移动的盘子数量
    int from, aux, to; // 参数：柱子索引 (0=A, 1=B, 2=C)
    int stage;         // 返回位置：0=刚进入, 1=第一次递归返回, 2=第二次递归返回
};

void hanoi_stack(int n, std::string rods[3])
{
    std::stack<Frame> stk;
    stk.push({n, 0, 1, 2, 0}); // 初始调用：从 A(0) 移到 C(2)，借助 B(1)

    while (!stk.empty())
    {
        Frame &f = stk.top();

        // 边界条件：只有一个盘子，直接移动
        if (f.step == 1)
        {
            rods[f.to].push_back(rods[f.from].back());
            rods[f.from].pop_back();
            stk.pop(); // 返回
            continue;
        }

        if (f.stage == 0)
        {
            // 阶段0：准备第一次递归 DFS(step-1, from, to, aux)
            f.stage = 1;
            stk.push({f.step - 1, f.from, f.to, f.aux, 0});
        }
        else if (f.stage == 1)
        {
            // 阶段1：第一次递归返回后，移动最底部的盘子
            rods[f.to].push_back(rods[f.from].back());
            rods[f.from].pop_back();

            // 准备第二次递归 DFS(step-1, aux, from, to)
            f.stage = 2;
            stk.push({f.step - 1, f.aux, f.from, f.to, 0});
        }
        else
        {
            // 阶段2：第二次递归返回后，当前帧完成
            stk.pop(); // 返回
        }
    }
}

int main()
{
    std::string rods[3] = {"987654321", "", ""};

    std::cout << "初始状态: A=" << rods[0] << " B=" << rods[1] << " C=" << rods[2] << std::endl;

    hanoi_stack(rods[0].size(), rods);

    std::cout << "最终状态: A=" << rods[0] << " B=" << rods[1] << " C=" << rods[2] << std::endl;

    return 0;
}