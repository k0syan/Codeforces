#include <iostream>
#include <vector>
typedef long long ll;
using namespace std;

int main() {
	int n;
	cin >> n;
	vector<ll> numbers;
	for (int i = 0; i < n; ++i) {
		ll tmp;
		cin >> tmp;
		numbers.push_back(tmp);
	}

	for (int i = 0; i < n / 2; ++i) {
		if (i % 2 == 0) {
			ll tmp = numbers[n - i - 1];
			numbers[n - i - 1] = numbers[i];
			numbers[i] = tmp;
		}
	}

	for (int i = 0; i < n; ++i) {
		cout << numbers[i];
		if (i != n - 1) {
			cout << " ";
		}
	}
	
	cout << endl;

	return 0;
}
