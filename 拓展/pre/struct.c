#include <stdio.h>
struct k{
    int a;
};

int main(){
    struct k m;
    printf("输入a的值");
    scanf("%d",&m.a);
    printf("%d",m.a);
    return 0;
}