#include <graphics.h>

void suspend() {
    initgraph(422, 750); // 初始化窗口大小为422*750
    setbkcolor(WHITE); // 设置背景
    cleardevice(); // 清屏

    // 绘制暂停界面文字

    // 设置字体颜色为蓝色
    settextcolor(BLUE);
    settextstyle(30, 0, _T("宋体"));
    outtextxy(130, 200, _T("游戏已暂停"));
    
    settextstyle(20, 0, _T("宋体"));
    outtextxy(150, 300, _T("按空格键继续"));

    // 用sleep暂停等待空格键按下
    while (!GetAsyncKeyState(VK_SPACE)) {   //当空格键未按下时
        Sleep(100); // 持续等待100毫秒
    }

    
    //按下空格键后会跳出等待循环，接着进入游戏就好

    //closegraph(); // 关闭图形窗口
    
}


int main() {
    suspend();
    return 0;
}