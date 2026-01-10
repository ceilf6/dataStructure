// #include "assistance.h"
#include <iostream>

void reversename(char *name, char *newname)
{
    char *p;
    p = strchr(name, ' ');
    *p = '\0';
    strcpy(newname, p + 1);
    strcat(newname, ",");
    strcat(newname, name);
    *p = ' ';
    return;
}

int main()
{
    char name[30], newname[30];
    std::cout << "输入一个人姓名：名在前，姓在后，中间有一个空格分隔。 " << std::endl;
    std::cin.getline(name, 30, '\n');
    reversename(name, newname);
    std::cout << "reversename :" << newname << std::endl;
    // system("PAUSE");
    return 0;
}
