#include <iostream>

// using namespace std;

int main()
{
    char s1[] = "It is a car";
    char s2[] = "jeep";
    char s3[] = "car";
    int result;
    char s4[20], *p;

    // 1. 长度（像string类型的话直接用 .size() 就好）
    std::cout << strlen(s1) << std::endl;

    // 2. 拷贝
    strcpy(s4, s2);
    std::cout << s4 << std::endl;

    // 3. 串连接
    strcat(s2, s3);
    std::cout << s2 << std::endl
              << s4 << std::endl;

    // 4. 串比较 - 字典序
    std::cout << strcmp(s2, s4) << std::endl;
    char s5[30] = "12";
    strcat(s5, s2);
    std::cout << strcmp(s5, s2) << std::endl; // '1' < 'j'

    // 5. 找首次符合目标的 idx （底层通过SIMD / 字宽并行扫描提高效率）
    char *idx = strchr(s1, 'i');
    std::cout << idx << std::endl; // idx是首次出现位置（包含），输出 is a car （会一直走到终止标识符号）

    return 0;
}