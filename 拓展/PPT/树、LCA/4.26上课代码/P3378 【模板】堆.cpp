#include <iostream>
#include <cstdio>

using namespace std;

typedef long long ll;
const int N = 1e6 + 50;

struct HEAP{
	int heap[N << 2], size;
	
	#define fa(x) (x >> 1)
	#define lson(x) (x << 1)
	#define rson(x) (x << 1 | 1) 
	
	void push(int x){
		heap[++size] = x;
		int pos = size;
		while(pos > 1 && heap[fa(pos)] > heap[pos]){
			swap(heap[fa(pos)], heap[pos]);
			pos = fa(pos);
		}
		return;
	}
	
	void pop(){
		swap(heap[1], heap[size]);
		size--;
		int pos = 1;
		while(lson(pos) <= size){
			int nxt = lson(pos);
			if(rson(pos) <= size && heap[rson(pos)] < heap[nxt]) nxt++;
			if(heap[nxt] < heap[pos]) swap(heap[nxt], heap[pos]);
			else break;
			pos = nxt;
		}
		return;
	}
	
	int top(){
		return heap[1];
	}
	
	bool empty(){
		return (size <= 0);
	}
	
}s;

int main(){
	ios::sync_with_stdio(false);
	cin.tie(0); cout.tie(0);
	int n;
	cin >> n;
	while(n--){
		int op, x;
		cin >> op;
		if(op == 1){
			cin >> x;
			s.push(x);
		}else if(op == 2) cout << s.top() << endl;
		else s.pop();
	}
	return 0;
} 