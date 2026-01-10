int main()
{
    int *ptr = malloc(sizeof(int));
    free(ptr);

    return 0;
    // malloc 不会调用构造函数, free 不会调用析构函数
}