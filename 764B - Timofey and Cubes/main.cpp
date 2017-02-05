#include <iostream>
#include <vector>
typedef long long ll;
using namespace std;

vector<ll> reverse(vector<ll> array, int start, int end) {
	while (start <= end) {
		ll tmp = array[start];
		array[start] = array[end];
	  array[end] = tmp;
	  ++start;
	  --end;
	}

	return array;
}

int main() {
	int n;
	cin >> n;
	vector<ll> numbers;
	for (int i = 0; i < n; ++i) {
		ll tmp;
		cin >> tmp;
		numbers.push_back(tmp);
	}

	int middle;
	if (n % 2 == 0) {
		middle = n / 2 - 1;
		numbers = reverse(numbers, middle, middle + 1);
		for(int i = 1; i < (n + 1) / 2; ++i) {
			numbers = reverse(numbers, middle - i, middle + i + 1);
		}
	} else {
		middle = n / 2;
		for(int i = 0; i < n / 2; ++i) {
			numbers = reverse(numbers, middle - i - 1, middle + i + 1);
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
