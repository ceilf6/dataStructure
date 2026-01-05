#include <iostream>
#include <fstream>

using namespace std;

int main()
{
    ofstream outFile("filePlay.out", ios::out);
    if (!outFile)
    {
        cerr << "cannot open filePlay.out" << endl;
    }
    int n = 2312;
    float m = 3994.0;
    outFile << "n: " << n << endl;
    outFile << "m: " << m << endl;
    return 0;
}