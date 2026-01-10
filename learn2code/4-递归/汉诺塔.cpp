#include <string>
#include <iostream>

void DFS(int step, std::string &from,
         std::string &aux,
         std::string &to)
{
    if (step == 1) // 边界条件，只有一个时直接 A->C
    {
        to.push_back(from.back());
        from.pop_back();
        return;
    }

    DFS(step - 1, from, to, aux); // from 除最后一个外暂存 aux 中

    // 由于 from 原先就是有序的，所以直接
    // 将 from 的最后一个放到 to 中
    to.push_back(from.back());
    from.pop_back();

    DFS(step - 1, aux, from, to); // 从 aux 中取回到 from
}

int main()
{
    std::string A = "987654321";
    std::string B = "";
    std::string C = "";

    const int LA = A.size();

    DFS(LA, A, B, C);

    std::cout << A << std::endl
              << B << std::endl
              << C << std::endl;

    return 0;
}