#include <iostream>
#include <functional>

double jifen(std::function<double(double)> f, double a, double b, int n) {
    double h = (b - a) / n;
    double total = 0.0;
    for (int i = 1; i < n; ++i) {
        total += f(a + i * h);
    }
    total = (0.5 * (f(a) + f(b)) + total) * h;
    return total;
}

double f(double x) {
    return 1.0;
}

int main() {
    std::cout << jifen(f, 1.0, 3.0, 1000) << std::endl;
    return 0;
}