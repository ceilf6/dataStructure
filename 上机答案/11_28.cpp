#include <iostream>
#include <string>
#include <stdexcept>
using namespace std;

// 链表节点类模板
template <typename T>
class Node
{
public:
    T data;     // 数据域
    Node *next; // 指针域

    // 构造函数
    Node(const T &value) : data(value), next(nullptr) {}
};

// 链表类模板
template <typename T>
class LinkedList
{
private:
    Node<T> *head; // 头指针
    int length;    // 链表长度

public:
    // 构造函数
    LinkedList() : head(nullptr), length(0) {}

    // 析构函数
    ~LinkedList()
    {
        clear();
    }

    // 清空链表
    void clear()
    {
        Node<T> *current = head;
        while (current != nullptr)
        {
            Node<T> *temp = current;
            current = current->next;
            delete temp;
        }
        head = nullptr;
        length = 0;
    }

    // 在链表末尾添加元素
    void append(const T &item)
    {
        Node<T> *newNode = new Node<T>(item);

        if (head == nullptr)
        {
            head = newNode;
        }
        else
        {
            Node<T> *current = head;
            while (current->next != nullptr)
            {
                current = current->next;
            }
            current->next = newNode;
        }
        length++;
    }

    // 根据索引获取元素
    T get(int index) const
    {
        if (index < 0 || index >= length)
        {
            throw out_of_range("索引越界");
        }

        Node<T> *current = head;
        for (int i = 0; i < index; i++)
        {
            current = current->next;
        }
        return current->data;
    }

    // 查找元素位置（返回索引，未找到返回-1）
    int find(const T &item) const
    {
        Node<T> *current = head;
        int index = 0;

        while (current != nullptr)
        {
            if (current->data == item)
            {
                return index;
            }
            current = current->next;
            index++;
        }
        return -1;
    }

    // 获取链表长度
    int size() const
    {
        return length;
    }

    // 判断链表是否为空
    bool isEmpty() const
    {
        return head == nullptr;
    }

    // 打印所有元素
    void display() const
    {
        Node<T> *current = head;
        while (current != nullptr)
        {
            cout << current->data;
            if (current->next != nullptr)
            {
                cout << " -> ";
            }
            current = current->next;
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

    // 获取从起始站到指定站的路径
    void getPath(const T &start, const T &end) const
    {
        int startIndex = find(start);
        int endIndex = find(end);

        if (startIndex == -1 || endIndex == -1)
        {
            throw invalid_argument("站点不存在");
        }

        cout << "路径: ";

        // 确定方向
        if (startIndex <= endIndex)
        {
            // 从前往后
            Node<T> *current = head;
            for (int i = 0; i < startIndex; i++)
            {
                current = current->next;
            }

            for (int i = startIndex; i <= endIndex; i++)
            {
                cout << current->data;
                if (i < endIndex)
                {
                    cout << " -> ";
                }
                current = current->next;
            }
        }
        else
        {
            // 从后往前（需要先收集节点）
            Node<T> *current = head;
            for (int i = 0; i < endIndex; i++)
            {
                current = current->next;
            }

            for (int i = endIndex; i <= startIndex; i++)
            {
                cout << current->data;
                if (i < startIndex)
                {
                    cout << " -> ";
                }
                current = current->next;
            }
        }
        cout << endl;
    }
};

int main()
{
    // 创建上海地铁7号线链表
    LinkedList<string> line7;

    // 添加上海地铁7号线站点（从南到北）
    line7.append("美兰湖");
    line7.append("罗南新村");
    line7.append("潘广路");
    line7.append("刘行");
    line7.append("顾村公园");
    line7.append("祁华路");
    line7.append("场中路");
    line7.append("大场镇");
    line7.append("行知路");
    line7.append("大华三路");
    line7.append("新村路");
    line7.append("岚皋路");
    line7.append("镇坪路");
    line7.append("长寿路");
    line7.append("昌平路");
    line7.append("静安寺");
    line7.append("常熟路");
    line7.append("肇嘉浜路");
    line7.append("东安路");
    line7.append("龙华中路");
    line7.append("后滩");
    line7.append("长清路");
    line7.append("耀华路");
    line7.append("云台路");
    line7.append("高科西路");
    line7.append("杨高南路");
    line7.append("锦绣路");
    line7.append("芳华路");
    line7.append("龙阳路");
    line7.append("花木路");

    cout << "=============== 上海地铁7号线站点信息 ===============" << endl;
    cout << "总站数: " << line7.size() << " 站" << endl;
    cout << "\n线路站点: " << endl;
    line7.display();

    cout << "\n=============== 查询功能演示 ===============" << endl;

    // 查询1: 延长路站是第几站（注意：7号线没有延长路站，这里用其他站点演示）
    string station1 = "静安寺";
    int position1 = line7.find(station1);
    if (position1 != -1)
    {
        cout << "\n查询1: \"" << station1 << "\" 站是第 " << (position1 + 1) << " 站（索引: " << position1 << "）" << endl;
    }
    else
    {
        cout << "\n查询1: \"" << station1 << "\" 站不在7号线上" << endl;
    }

    // 查询2: 从静安寺到肇嘉浜路需要乘坐几站
    string startStation = "静安寺";
    string endStation = "肇嘉浜路";
    try
    {
        int stations = line7.stationsBetween(startStation, endStation);
        cout << "\n查询2: 从 \"" << startStation << "\" 到 \"" << endStation << "\" 需要乘坐 " << stations << " 站" << endl;

        int startPos = line7.find(startStation);
        int endPos = line7.find(endStation);
        cout << "       (" << startStation << "是第" << (startPos + 1) << "站，"
             << endStation << "是第" << (endPos + 1) << "站)" << endl;

        // 显示路径
        cout << "       ";
        line7.getPath(startStation, endStation);
    }
    catch (const exception &e)
    {
        cout << "查询错误: " << e.what() << endl;
    }

    // 查询3: 从美兰湖到花木路需要乘坐几站
    string start3 = "美兰湖";
    string end3 = "花木路";
    try
    {
        int stations3 = line7.stationsBetween(start3, end3);
        cout << "\n查询3: 从 \"" << start3 << "\" 到 \"" << end3 << "\" 需要乘坐 " << stations3 << " 站（全程）" << endl;
    }
    catch (const exception &e)
    {
        cout << "查询错误: " << e.what() << endl;
    }

    // 查询4: 龙阳路是第几站
    string station4 = "龙阳路";
    int position4 = line7.find(station4);
    if (position4 != -1)
    {
        cout << "\n查询4: \"" << station4 << "\" 站是第 " << (position4 + 1) << " 站" << endl;
    }

    // 查询5: 从镇坪路到龙华中路需要乘坐几站
    string start5 = "镇坪路";
    string end5 = "龙华中路";
    try
    {
        int stations5 = line7.stationsBetween(start5, end5);
        cout << "\n查询5: 从 \"" << start5 << "\" 到 \"" << end5 << "\" 需要乘坐 " << stations5 << " 站" << endl;
        cout << "       ";
        line7.getPath(start5, end5);
    }
    catch (const exception &e)
    {
        cout << "查询错误: " << e.what() << endl;
    }

    // 查询6: 从顾村公园到静安寺需要乘坐几站
    string start6 = "顾村公园";
    string end6 = "静安寺";
    try
    {
        int stations6 = line7.stationsBetween(start6, end6);
        cout << "\n查询6: 从 \"" << start6 << "\" 到 \"" << end6 << "\" 需要乘坐 " << stations6 << " 站" << endl;
        cout << "       ";
        line7.getPath(start6, end6);
    }
    catch (const exception &e)
    {
        cout << "查询错误: " << e.what() << endl;
    }

    // 查询7: 从后滩到大场镇需要乘坐几站
    string start7 = "后滩";
    string end7 = "大场镇";
    try
    {
        int stations7 = line7.stationsBetween(start7, end7);
        cout << "\n查询7: 从 \"" << start7 << "\" 到 \"" << end7 << "\" 需要乘坐 " << stations7 << " 站" << endl;
    }
    catch (const exception &e)
    {
        cout << "查询错误: " << e.what() << endl;
    }

    cout << "\n===============================================" << endl;

    // 测试链表的其他功能
    cout << "\n=============== 链表基本操作测试 ===============" << endl;

    cout << "\n获取第10站的站名: " << line7.get(9) << endl;
    cout << "获取第20站的站名: " << line7.get(19) << endl;

    cout << "\n链表是否为空: " << (line7.isEmpty() ? "是" : "否") << endl;
    cout << "链表长度: " << line7.size() << " 站" << endl;

    cout << "\n===============================================" << endl;

    return 0;
}
