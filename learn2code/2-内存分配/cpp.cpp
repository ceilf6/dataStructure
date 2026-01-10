int main()
{
    int *ptr = new int;
    delete ptr;

    int *p = new int[10];
    delete[] p;

    /*
    更安全是用 memory 库
    #include <memory>

    std::unique_ptr<int> p = std::make_unique<int>();
    */

    return 0;
}