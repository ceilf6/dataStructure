#include <iostream>
#include <string>
#include <stdexcept>
using namespace std;

// 顺序表类模板
template <typename T>
class SeqList
{
private:
    T *data;      // 动态数组存储数据
    int capacity; // 容量
    int length;   // 当前长度

    // 扩容函数
    void resize()
    {
        capacity *= 2;
        T *newData = new T[capacity];
        for (int i = 0; i < length; i++)
        {
            newData[i] = data[i];
        }
        delete[] data;
        data = newData;
    }

public:
    // 构造函数
    SeqList(int cap = 10) : capacity(cap), length(0)
    {
        data = new T[capacity];
    }

    // 析构函数
    ~SeqList()
    {
        delete[] data;
    }

    // 插入元素到末尾
    void append(const T &item)
    {
        if (length >= capacity)
        {
            resize();
        }
        data[length++] = item;
    }

    // 获取元素
    T get(int index) const
    {
        if (index < 0 || index >= length)
        {
            throw out_of_range("索引越界");
        }
        return data[index];
    }

    // 查找元素位置（返回索引，未找到返回-1）
    int find(const T &item) const
    {
        for (int i = 0; i < length; i++)
        {
            if (data[i] == item)
            {
                return i;
            }
        }
        return -1;
    }

    // 获取长度
    int size() const
    {
        return length;
    }

    // 判断是否为空
    bool isEmpty() const
    {
        return length == 0;
    }

    // 打印所有元素
    void display() const
    {
        for (int i = 0; i < length; i++)
        {
            cout << data[i];
            if (i < length - 1)
                cout << " -> ";
        }
        cout << endl;
    }

    // 计算两个站点之间的距离
    int distance(const T &start, const T &end) const
    {
        int startIndex = find(start);
        int endIndex = find(end);

        if (startIndex == -1 || endIndex == -1)
        {
            throw invalid_argument("站点不存在");
        }

        return abs(endIndex - startIndex);
    }

    // 获取某站点到另一站点需要经过的站数
    int stationsBetween(const T &start, const T &end) const
    {
        return distance(start, end);
    }
};

int main()
{
    // 创建上海地铁1号线顺序表
    SeqList<string> line1;

    // 添加上海地铁1号线站点（从北往南）
    line1.append("莘庄");
    line1.append("外环路");
    line1.append("莲花路");
    line1.append("锦江乐园");
    line1.append("上海南站");
    line1.append("漕宝路");
    line1.append("上海体育馆");
    line1.append("徐家汇");
    line1.append("衡山路");
    line1.append("常熟路");
    line1.append("陕西南路");
    line1.append("黄陂南路");
    line1.append("人民广场");
    line1.append("新闸路");
    line1.append("汉中路");
    line1.append("上海火车站");
    line1.append("中山北路");
    line1.append("延长路");
    line1.append("上海马戏城");
    line1.append("汶水路");
    line1.append("彭浦新村");
    line1.append("共康路");
    line1.append("通河新村");
    line1.append("呼兰路");
    line1.append("共富新村");
    line1.append("宝安公路");
    line1.append("友谊西路");
    line1.append("富锦路");

    cout << "=============== 上海地铁1号线站点信息 ===============" << endl;
    cout << "总站数: " << line1.size() << " 站" << endl;
    cout << "\n线路站点: " << endl;
    line1.display();

    cout << "\n=============== 查询功能演示 ===============" << endl;

    // 查询1: 延长路站是第几站
    string station1 = "延长路";
    int position1 = line1.find(station1);
    if (position1 != -1)
    {
        cout << "\n查询1: \"" << station1 << "\" 站是第 " << (position1 + 1) << " 站（索引: " << position1 << "）" << endl;
    }

    // 查询2: 从延长路到徐家汇需要乘坐几站
    string startStation = "延长路";
    string endStation = "徐家汇";
    try
    {
        int stations = line1.stationsBetween(startStation, endStation);
        cout << "\n查询2: 从 \"" << startStation << "\" 到 \"" << endStation << "\" 需要乘坐 " << stations << " 站" << endl;

        int startPos = line1.find(startStation);
        int endPos = line1.find(endStation);
        cout << "       (" << startStation << "是第" << (startPos + 1) << "站，"
             << endStation << "是第" << (endPos + 1) << "站)" << endl;
    }
    catch (const exception &e)
    {
        cout << "查询错误: " << e.what() << endl;
    }

    // 查询3: 从莘庄到富锦路需要乘坐几站
    string start3 = "莘庄";
    string end3 = "富锦路";
    try
    {
        int stations3 = line1.stationsBetween(start3, end3);
        cout << "\n查询3: 从 \"" << start3 << "\" 到 \"" << end3 << "\" 需要乘坐 " << stations3 << " 站" << endl;
    }
    catch (const exception &e)
    {
        cout << "查询错误: " << e.what() << endl;
    }

    // 查询4: 人民广场是第几站
    string station4 = "人民广场";
    int position4 = line1.find(station4);
    if (position4 != -1)
    {
        cout << "\n查询4: \"" << station4 << "\" 站是第 " << (position4 + 1) << " 站" << endl;
    }

    // 查询5: 从上海南站到上海火车站需要乘坐几站
    string start5 = "上海南站";
    string end5 = "上海火车站";
    try
    {
        int stations5 = line1.stationsBetween(start5, end5);
        cout << "\n查询5: 从 \"" << start5 << "\" 到 \"" << end5 << "\" 需要乘坐 " << stations5 << " 站" << endl;
    }
    catch (const exception &e)
    {
        cout << "查询错误: " << e.what() << endl;
    }

    cout << "\n===============================================" << endl;

    return 0;
}