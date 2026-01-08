#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "graphics.h"  // 引入 EasyX 图形库的头文件
#include <Windows.h>   // 引入 Windows API 头文件

#define MAX_PLAYERS 20  // 显示的最大玩家数量

typedef struct {
    char name[20];
    int score;
} Player;

Player leaderboard[MAX_PLAYERS];

// 比较函数
int comparePlayers(const void* a, const void* b) {
    return ((Player*)b)->score - ((Player*)a)->score;
}

void updateLeaderboard(Player* players, int numPlayers) {
    // 复制玩家数据到排行榜数组
    memcpy(leaderboard, players, numPlayers * sizeof(Player));

    // 排序排行榜：qsort函数交换
    qsort(leaderboard, numPlayers, sizeof(Player), comparePlayers);
}

void board() {
    initgraph(422, 750);  // 初始化图形窗口大小

    settextstyle(20, 0, _T("宋体"));  // 设置字体样式
    setbkmode(TRANSPARENT);            // 设置背景

    // 绘制标题
    outtext(_T("飞机大战排行榜"));

    // 绘制排行榜内容
    char buffer[50];
    for (int i = 0; i < MAX_PLAYERS; i++) {
        sprintf_s(buffer, sizeof(buffer), "%d. %s - %d", i + 1, leaderboard[i].name, leaderboard[i].score);
        outtextxy(100, 50 + i * 30, buffer);
    }

    // 等待用户点击关闭按钮
    while (!GetAsyncKeyState(VK_ESCAPE)) {
        Sleep(100);
    }

    closegraph();  // 关闭图形窗口
}


int main() {

    // 先更新排行榜
    updateLeaderboard(players, MAX_PLAYERS);

    //然后再调用打印函数
    board();

    return 0;
}