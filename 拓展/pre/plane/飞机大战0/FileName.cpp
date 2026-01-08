#include <stdio.h>
#include <easyx.h>
#include <stdlib.h>
#include <graphics.h>
#include <Windows.h>
#include <time.h>
#include <conio.h>
#include <mmsystem.h>
#pragma comment(lib,"winmm.lib")
#pragma comment( lib, "MSIMG32.LIB")
#define MAX 100
#define MAX_PLAYERS 20  // 显示的最大玩家数量

IMAGE BOSS;
IMAGE ZHANJI;
IMAGE DIJI;
IMAGE JINGYING;
IMAGE ZIDAN;
IMAGE HEDAN;
IMAGE MYZIDAN;
int jiemian_x = 422;    //界面宽度
int jiemian_y = 750;    //界面长度
const clock_t FPS = 1000 / 60;    //每一帧应该花费的时间
int speed = 10;  //定义我方战机移动速度
int zidan_w = 25;   //定义子弹宽度
int zidan_h = 25;   //定义子弹长度
int zidan_sh = 10;  //定义子弹伤害
int hedan_sh = 100; //定义核弹伤害
int w = 50; //定义战机宽度
int h = 50; //定义战机高度
int x = 200;    //定义战机x坐标
int y = 700;    //定义战机y坐标
int hp = 1000;
ExMessage msg = { 0 };
int i = 0;
typedef struct {
    char name[20];
    int score;
} Player;
Player leaderboard[MAX_PLAYERS];
int comparePlayers(const void* a, const void* b) {
    return ((Player*)b)->score - ((Player*)a)->score;
}

void updateLeaderboard(Player* players, int numPlayers) {
    // 复制玩家数据到排行榜数组
    memcpy(leaderboard, players, numPlayers * sizeof(Player));

    // 排序排行榜：qsort函数交换
    qsort(leaderboard, numPlayers, sizeof(Player), comparePlayers);
}
typedef struct
{
	int x;
	int y;
	int a;  // 是否有出场权
	int hp; //血量
	int speed;  //速度
}qwe;   //定义敌机的参数
typedef struct
{
	int x;
	int y;
	int a;
	int hp;
	int speed;
}asd;   //定义精英敌机的参数
typedef struct
{
	int x;
	int y;
	int w;
	int hp;
	int h;
	int a;
	int speed;
}zxc;   //定义boss敌机的参数
typedef struct
{
	int x;
	int y;
	int a;
	int m;  //标识符，0代表属于敌方，1代表属于我方
}rty;   //定义敌方子弹参数
typedef struct
{
	int x;
	int y;
	int a;
}fgh;   //定义核弹参数
zxc boss[10];
rty zidan[2 * MAX];
fgh hedan[MAX];
asd jingying[MAX] = { 0 };
qwe diji[MAX] = { 0 };
int dan_speed;
void transparentimage3(IMAGE* dstimg, int x, int y, IMAGE* srcimg);
void transparentimage3(IMAGE* dstimg, int x, int y, IMAGE* srcimg) //新版png
{
	HDC dstDC = GetImageHDC(dstimg);
	HDC srcDC = GetImageHDC(srcimg);
	int w = srcimg->getwidth();
	int h = srcimg->getheight();
	BLENDFUNCTION bf = { AC_SRC_OVER, 0, 255, AC_SRC_ALPHA };
	AlphaBlend(dstDC, x, y, w, h, srcDC, 0, 0, w, h, bf);
}//输出透明贴图函数
void Game_Fighter(void);    //游戏界面函数
void chushihua_diji(void);  //敌机初始化函数
void gengxin_diji(void);    //敌机参数更新函数
void chuchangquan_diji(void);   //敌机出场权函数
void shifouxiaoshi_diji(void);      //敌机是否消失函数
void yidong_zhanji(void);   //我方战机移动函数
void chuchangquan_jingying(void);//精英敌机出场权函数
//void chuchangquan_boss(void);   //boss出场权函数
void dayinjiemian(int);   //打印界面函数
void danchuchangquan(void); //子弹核弹出场权函数
void mydanchuchangquan(void);   //我方子弹出场权函数
void hetiao(void);  //boss横跳函数
void kouxue(void);  //扣血机制函数
void kouxue(void)
{
    int i = 0;
    int j;
    for (i = 0; i < 2 * MAX; i++)
    {
        if (i < MAX)
        {
            if (hedan[i].a)
            {
                int m_x = (hedan[i].x * 2 + w) / 2;
                int m_y = hedan[i].y;
                if (m_x <= x + w && m_x > x && m_y <= y + h && m_y >= y)
                    hp--;
            }
        }
        if (zidan[i].a)
        {
            if (zidan[i].m)
            {
                int m_x = (zidan[i].x * 2 + zidan_w) / 2;
                int m_y = zidan[i].y;
                if (m_x >= boss[0].x && m_x <= boss[0].x + boss[0].w && m_y <= boss[0].y + boss[0].h && m_y >= boss[0].y && boss[0].a)
                {
                    boss[0].hp--;
                    continue;
                }
                for (j = 0; j < MAX; j++)
                {
                    if (diji[j].a || jingying[j].a)
                    {
                        if (m_x >= diji[j].x && m_x <= diji[j].x + w && m_y <= diji[j].y + h && m_y >= diji[j].y && diji[i].a)
                        {
                            diji[j].hp--;
                            break;
                        }
                        if (m_x >= jingying[j].x && m_x <= jingying[j].x + w && m_y <= jingying[j].y + h && m_y >= jingying[j].y && jingying[i].a)
                        {
                            jingying[j].hp--;
                            break;
                        }

                    }
                }
            }
            if (!zidan[i].m)
            {
                int m_x = (zidan[i].x * 2 + zidan_w) / 2;
                int m_y = zidan[i].y;
                if (m_x <= x + w && m_x > x && m_y <= y + h && m_y >= y)
                    hp--;
            }
        }
    }
}
void mydanchuchangquan(void)
{
    for (int j = 0; j < 2 * MAX; j++)
    {
        if (!zidan[j].a && !zidan[j].m)
        {
            zidan[j].a = 1;
            zidan[j].m = 1;
            zidan[j].x = x + (w - zidan_w) / 2;
            zidan[j].y = y;
            break;
        }
    }
}
void hetiao(void)
{
    if (boss[0].a)
    {
        boss[0].x += boss[0].speed;
        boss[0].x %= jiemian_x - boss[0].w;
    }
}
void danchuchangquan(void)
{
    if (boss[0].a)
    {
        for (int i = 0; i < MAX; i++)
        {
            if (!hedan[i].a)
            {
                hedan[i].x = boss[0].x + (boss[0].w - w) / 2;
                hedan[i].y = boss[0].y + boss[0].h;
                hedan[i].a = 1;
                break;
            }
        }
    }
    for (int i = 0; i < MAX; i++)
    {
        if (diji[i].a)
        {
            for (int j = 0; j < 2 * MAX; j++)
            {
                if (!zidan[j].a)
                {
                    zidan[j].a = 1;
                    zidan[j].x = diji[i].x + (w - zidan_w) / 2;
                    zidan[j].y = diji[i].y + h;
                    break;
                }
            }
        }
        if (jingying[i].a)
        {
            for (int j = 0; j < 2 * MAX; j++)
            {
                if (!zidan[j].a)
                {
                    zidan[j].a = 1;
                    zidan[j].x = jingying[i].x + (w - zidan_w) / 2;
                    zidan[j].y = jingying[i].y + h;
                    break;
                }
            }
        }
    }
}
void dayinjiemian(int k)
{
    //static int m = 0;   //标识符
    cleardevice();
    IMAGE background;
    loadimage(&background, "./menu1.jpg");
    putimage(0, 0, &background);
    if (k % 1800 == 0 && boss[0].a == 0)
    {
        transparentimage3(NULL, boss[0].x, boss[0].y, &BOSS);
        boss[0].a = 1;
    }//30秒生成一个boss
    if (boss[0].a)
    {
        transparentimage3(NULL, boss[0].x, boss[0].y, &BOSS);
    }
    transparentimage3(NULL, x, y, &ZHANJI);     //打印我方战机
    for (int i = 0; i < MAX; i++)   //打印敌方战机
    {
        if (diji[i].a)
            transparentimage3(NULL, diji[i].x, diji[i].y, &DIJI);
        if (jingying[i].a)
            transparentimage3(NULL, jingying[i].x, jingying[i].y, &JINGYING);
        if (hedan[i].a)
            transparentimage3(NULL, hedan[i].x, hedan[i].y, &HEDAN);
    }
    for (int i = 0; i < 2 * MAX; i++)
    {
        if (zidan[i].a && !zidan[i].m)
            transparentimage3(NULL, zidan[i].x, zidan[i].y, &ZIDAN);
        if (zidan[i].a && zidan[i].m)
            transparentimage3(NULL, zidan[i].x, zidan[i].y, &MYZIDAN);
    }
}
void chushihua_diji(void) //敌机初始化函数
{
    int i;
    srand(time(NULL));
    for (i = 0; i < MAX; i++)
    {
        diji[i].x = rand() % (jiemian_x - w);
        diji[i].y = rand() % (jiemian_y / 4);
        diji[i].a = 0;
        diji[i].hp = 1;
        diji[i].speed = 1;
        jingying[i].x = rand() % (jiemian_x - w);
        jingying[i].y = rand() % (jiemian_y / 4);
        jingying[i].a = 0;
        jingying[i].hp = 2;
        jingying[i].speed = 1;
        hedan[i].a = 0;
    }
    for (int i = 0; i < 2 * MAX; i++)
    {
        zidan[i].a = 0;
        zidan[i].m = 0;
    }
    boss[0].x = ((jiemian_x - w) / 2);
    boss[0].y = (jiemian_y / 5);
    boss[0].hp = 1000;
    boss[0].w = 100;
    boss[0].h = 100;
    boss[0].a = 0;
    boss[0].speed = 10;
    loadimage(&BOSS, "tupian/boss.png", boss[0].w, boss[0].h);
    loadimage(&ZHANJI, "tupian/zhanji.png", w, h);
    loadimage(&DIJI, "tupian/diji.png", w, h);
    loadimage(&JINGYING, "tupian/jingying.png", w, h);
    dan_speed = 2 * diji[0].speed;
    loadimage(&ZIDAN, "tupian/zidan.png", zidan_w, zidan_h);
    loadimage(&HEDAN, "tupian/hedan.png", w, h);
    loadimage(&MYZIDAN, "tupian/myzidan.png", zidan_w, zidan_h);
}
void Game_Fighter(void) //游戏界面函数
{
    int starttime;
    int endtime;
    int k = 1;  //计数器
    int m = 0;//boss技能启动装置
    cleardevice();
    chushihua_diji();
    while (true)
    {
       /* mciSendString("open ./background.WMA", NULL, 0, NULL);
        mciSendString("play ./background.WMA", NULL, 0, NULL);*/
        starttime = clock();
        BeginBatchDraw();
       
        dayinjiemian(k);
        FlushBatchDraw();
        peekmessage(&msg, EX_KEY);
        k %= 1800;
        k++;
        //printf("%d\n",k);
        if (k % 10 == 0)//每隔一秒就自动生成一个敌机
        {
            if (k % 600 == 0 && !m)
                m = 1;
            if (m)
            {
                m++;
                hetiao();
                if ((m - 1) % ((jiemian_x) / 10) == 0)
                    m = 0;
            }
            mydanchuchangquan();
            if (k % 30 == 0)
                danchuchangquan();
            if (k % 300 == 0)
                chuchangquan_jingying();
            if (k % 600 == 0 && diji[0].speed < 4)//到一定速度之后，速度将不再变化
            {
                for (int i = 0; i < MAX; i++)
                {
                    diji[i].speed++;
                    jingying[i].speed++;
                }  //每隔10秒敌机速度加一
                dan_speed++;
            }
            if (k % 60 == 0)
                chuchangquan_diji();
        }
        yidong_zhanji();
        gengxin_diji();
        kouxue();
        shifouxiaoshi_diji();
        msg.message = 0;
        //printf("%d\n",k);
        endtime = clock();
        Sleep(endtime - starttime);
    }
}

void gengxin_diji(void)//敌机参数更新函数
{
    for (int i = 0; i < MAX; i++)
    {
        if (diji[i].a)
            diji[i].y += diji[i].speed;
        if (jingying[i].a)
            jingying[i].y += jingying[i].speed;
        if (hedan[i].a)
            hedan[i].y += dan_speed;
    }
    for (int i = 0; i < 2 * MAX; i++)
    {
        if (zidan[i].a && !zidan[i].m)
            zidan[i].y += dan_speed;
        if (zidan[i].a && zidan[i].m)
            zidan[i].y -= dan_speed;
    }
}


void chuchangquan_diji(void)//敌机出场权函数
{
    for (int i = 0; i < MAX; i++)
    {
        if (!diji[i].a)
        {
            diji[i].a = 1;
            break;
        }
    }
}

void chuchangquan_jingying(void)//精英敌机出场权函数
{
    for (int i = 0; i < MAX; i++)
    {
        if (!jingying[i].a)
        {
            jingying[i].a = 1;
            break;
        }
    }
}

//void chuchangquan_boss(void)   //boss出场权函数
//{
//    for (int i = 0; i < 10; i++)
//    {
//        if (!boss[i].a)
//        {
//            boss[i].a = 1;
//            break;
//        }
//    }
//}

void shifouxiaoshi_diji(void)//敌机是否消失函数
{
    if (boss[0].hp <= 0)
    {
        boss[0].a = 0;
        boss[0].hp = 1000;
    }
    for (int i = 0; i < MAX; i++)
    {
        if (diji[i].a)
        {
            if (diji[i].y + h >= jiemian_y || diji[i].hp <= 0)
            {
                diji[i].a = 0;
                diji[i].x = rand() % (jiemian_x - w);
                diji[i].y = rand() % (jiemian_y / 4);
                diji[i].hp = 1;
            }
        }
        if (jingying[i].a)
        {
            if (jingying[i].y + h >= jiemian_y || jingying[i].hp <= 0)
            {
                jingying[i].a = 0;
                jingying[i].x = rand() % (jiemian_x - w);
                jingying[i].y = rand() % (jiemian_y / 4);
                jingying[i].hp = 2;
            }
        }
        if (hedan[i].a)
        {
            if (hedan[i].y + h >= jiemian_y)
            {
                hedan[i].a = 0;
            }
        }
    }
    for (int i = 0; i < 2 * MAX; i++)
    {
        if (zidan[i].a && !zidan[i].m)
        {
            if (zidan[i].y + zidan_h >= jiemian_y)
            {
                zidan[i].a = 0;
            }
        }
        if (zidan[i].a && zidan[i].m)
        {
            if (zidan[i].y <= 0)
            {
                zidan[i].a = 0;
                zidan[i].m = 0;
            }
        }
    }
}

void yidong_zhanji(void)//我方战机移动函数
{
    if (msg.message == WM_KEYDOWN)
    {
        switch (msg.vkcode)
        {
        case 'W':
            y -= speed;
            break;
        case 'S':
            y += speed;
            break;
        case 'A':
            x -= speed;
            break;
        case 'D':
            x += speed;
        }
    }
}
void menu();
void PlayGame(void);
void shubiao();
void checkshubiao();
void board();
void finish();
void Developer();
void gameintroduce();
void botton(int x,int y,int w,int h);
bool shifou(int x, int y, int w, int h);
void checkpoint();
void nomal_botton(int left, int top, int right, int bottom, const char* text)//正常状态按钮
{
	setbkmode(TRANSPARENT);//设置字体背景透明
	char lingshi_text[50] = { 0 };//按钮内容
	strcpy(lingshi_text, text);//获取内容
	settextstyle(35, 20, "微软雅黑");//设置字体
	settextcolor(BLACK);
	int text_x = left + (right - left - textwidth(lingshi_text)) / 2;//内容横坐标
	int text_y = top + (bottom - top - textheight(lingshi_text)) / 2;//内容纵坐标
	outtextxy(text_x, text_y, lingshi_text);
}
void menu()
{
	IMAGE img_mm;
	loadimage(&img_mm, "./menu1.jpg");
	putimage(0, 0, &img_mm);
	HWND startwindow = GetHWnd();//获取窗口句柄
	SetWindowText(startwindow, "飞机大战");//设置窗口标题
	BeginBatchDraw();
	botton(100, 100, 233, 40);//第一个按钮
	nomal_botton(100,100,333,140,"选择关卡");
	botton(100, 200, 233, 40);//第二个按钮
	nomal_botton(100, 200, 333, 240, "排行榜");
	botton(100, 300, 233, 40);//第三个按钮
	nomal_botton(100, 300, 333, 340, "游戏介绍");
	botton(100, 400, 233, 40);//第四个按钮
	nomal_botton(100, 400, 333, 440, "开发人员");
	botton(100, 500, 233, 40);//第四个按钮
	nomal_botton(100, 500, 333, 540, "退出游戏");
	FlushBatchDraw();
	shubiao();
}
void botton(int x, int y, int w, int h)
{
	setlinecolor(BLACK);
	setfillcolor(RGB(195, 201, 201));
	fillroundrect(x, y, x + w, y + h, 5, 5);
}
void shubiao(void)
{
	while (true)
	{

		//存放矩形相关参数

		if (peekmessage(&msg, EX_MOUSE))
		{
			if (msg.message == WM_LBUTTONDOWN && shifou(100, 100, 233, 40))  //诺鼠标在对应矩形内且按下左键的话，将要跳转当相应界面
			{

				checkpoint();          //关卡选择界面
				break;
			}
			if (msg.message == WM_LBUTTONDOWN && shifou(100, 200, 233, 40))  //诺鼠标在对应矩形内且按下左键的话，将要跳转当相应界面
			{
				board();
				break;
			}
			if (msg.message == WM_LBUTTONDOWN && shifou(100, 300, 233, 40))  //诺鼠标在对应矩形内且按下左键的话，将要跳转当相应界面
			{
				gameintroduce();
				break;
			}
			if (msg.message == WM_LBUTTONDOWN && shifou(100, 400, 233, 40))  //诺鼠标在对应矩形内且按下左键的话，将要跳转当相应界面
			{
				Developer();
				break;
			}
			if (msg.message == WM_LBUTTONDOWN && shifou(100, 500, 333, 40))  //诺鼠标在对应矩形内且按下左键的话，将要跳转当相应界面
			{
				finish();//退出游戏
				break;
			}
			
			
		}
	}
}
void checkshubiao()
{
	while (true)
	{
		if (peekmessage(&msg, EX_MOUSE))
		{
			if (msg.message == WM_LBUTTONDOWN && shifou(100, 100, 233, 40))  //诺鼠标在对应矩形内且按下左键的话，将要跳转当相应界面
			{
                mciSendString("close BGM", 0, 0, 0);
                Game_Fighter();
				//修改参数，跳转游戏页面
				break;
			}
			if (msg.message == WM_LBUTTONDOWN && shifou(100, 200, 233, 40))  //诺鼠标在对应矩形内且按下左键的话，将要跳转当相应界面
			{
                mciSendString("close BGM", 0, 0, 0);
                Game_Fighter();
				//修改参数，跳转游戏页面
				break;
			}
			if (msg.message == WM_LBUTTONDOWN && shifou(100, 300, 233, 40))  //诺鼠标在对应矩形内且按下左键的话，将要跳转当相应界面
			{
                mciSendString("close BGM", 0, 0, 0);
                Game_Fighter();
				//修改参数，跳转游戏页面
				
				break;
			}
			if (msg.message == WM_LBUTTONDOWN && shifou(100, 400, 233, 40))  //诺鼠标在对应矩形内且按下左键的话，将要跳转当相应界面
			{
                mciSendString("close BGM", 0, 0, 0);
				//修改参数，跳转游戏页面        //音量调节界面
				
				break;
			}
			if (msg.message == WM_LBUTTONDOWN && shifou(100, 500, 333, 40))  //诺鼠标在对应矩形内且按下左键的话，将要跳转当相应界面
			{
				menu();
				break;
			}
			

		}
	}
}
bool shifou(int x, int y, int w, int h)
{
	if (msg.x >= x && msg.x <= x + w && msg.y >= y && msg.y <= y + h)
		return true;
	return false;
}
void board() {
    cleardevice();
    IMAGE background;
    loadimage(&background, "./menu1.jpg");
    putimage(0, 0, &background);
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

    
}
void finish()
{
	exit(0);
}
void checkpoint()
{
    if (msg.message == WM_LBUTTONDOWN && shifou(100, 100, 233, 40))  //诺鼠标在对应矩形内且按下左键的话，将要跳转当相应界面
    {
        cleardevice();
        IMAGE img_ss;
        loadimage(&img_ss, "./menu1.jpg");
        putimage(0, 0, &img_ss);
        while (1)
        {
            BeginBatchDraw();
            botton(100, 100, 233, 40);//第一个按钮
            nomal_botton(100, 100, 333, 140, "有手就行");
            botton(100, 200, 233, 40);//第二个按钮
            nomal_botton(100, 200, 333, 240, "就这水平");
            botton(100, 300, 233, 40);//第三个按钮
            nomal_botton(100, 300, 333, 340, "有点东西");
            botton(100, 400, 233, 40);//第四个按钮
            nomal_botton(100, 400, 333, 440, "有亿点难");
            botton(100, 500, 233, 40);//第四个按钮
            nomal_botton(100, 500, 333, 540, "返回菜单");
            FlushBatchDraw();
            checkshubiao();
        }
	}

}
void gameintroduce()
{
	    cleardevice();
		IMAGE background;
		loadimage(&background, "./menu1.jpg");
		putimage(0, 0, &background);
		
			outtextxy(140, 20, "游戏简介");
			settextstyle(20, 0, "宋文");
			outtextxy(0, 60, "飞机大战游戏是以太空主题的画面为游戏背景。");
			outtextxy(0, 80, "拟三体世界观的设定,是一个简洁流畅,游戏方式");
			outtextxy(0, 100, "式简单的小游戏，由玩家通过鼠标控制我方战机");
			outtextxy(0, 120, "通过鼠标控制我方战机向三体文明发动进攻。战");
			outtextxy(0, 140, "战机初始有一定量的血量，屏幕上随机产生敌机，");
			outtextxy(0, 160, "战机产生的数量和当前关卡难度有关，关卡越难");
			outtextxy(0, 180, "产生的敌机越多，游戏难度越大，玩家可通过氪");
			outtextxy(0, 200, "金降低游戏难度。游戏过程中玩家需要操作战机");
			outtextxy(0, 220, "躲避敌方子弹，战机可拾取装备提升战力。我方战机与敌机只要");
			outtextxy(0, 240, "中弹都会减血，直至血槽为空，战机爆炸，关卡");
			outtextxy(0, 260, "内所有敌机爆炸后通关，全部关卡通过后游戏结");
			outtextxy(0, 280, "束。");
			
			BeginBatchDraw();
			botton(230, 700, 180, 40);
			nomal_botton(230, 700, 410, 740, "返回菜单");
			FlushBatchDraw();
			while (1)
			{
				if (peekmessage(&msg, EX_MOUSE))
				{
					if (msg.message == WM_LBUTTONDOWN && shifou(230, 700, 180, 40))  //诺鼠标在对应矩形内且按下左键的话，将要跳转当相应界面
					{
						menu();
						break;
					}
				}
			}
}
void Developer() {
	
	cleardevice();
	IMAGE background;
	loadimage(&background, "./menu1.jpg");
	putimage(0, 0, &background);
	settextstyle(40, 0, "微软雅黑");
	BeginBatchDraw();
	outtextxy(130, 20, "开发人员介绍");
	outtextxy(20, 60, "组长：冷雨");
	outtextxy(20, 100, "副组长：brain 云淡风轻");
	outtextxy(20, 140, "技术官：墨小菲 10世界 自隶");
	outtextxy(20, 180, "产品经理：奶黄包");
	outtextxy(20, 220, "监督官：云淡风轻");
	outtextxy(20, 260, "信息官：brain");
	botton(230, 700, 180, 40);
	nomal_botton(230, 700, 410, 740, "返回菜单");
		FlushBatchDraw();
		while(1)
		{
		if (peekmessage(&msg, EX_MOUSE))
		{
			if (msg.message == WM_LBUTTONDOWN && shifou(230, 700, 180, 40))  //诺鼠标在对应矩形内且按下左键的话，将要跳转当相应界面
			{
				menu();
				break;
			}
		}
	}
}

int main()
{
	//创建一个图形窗口 宽度*高度
	initgraph(422,750,EX_SHOWCONSOLE);//400x600
	setbkcolor(WHITE);

	cleardevice();
   mciSendString("open ./background.WMA alias BGM", 0, 0, 0);
    mciSendString("play BGM repeat", 0, 0, 0);
    //mciSendString("open ./background.WMA", NULL, 0, NULL);
   // mciSendString("play ./background.WMA", NULL, 0, NULL);
	menu();
	getchar();
	closegraph();
	return 0;
}