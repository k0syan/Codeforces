#include <iostream>
#include <vector>
using namespace std;

typedef long long ll;

int main() {
  int n;
  cin >> n;
  vector<ll> cubes;
  for (int i = 0; i < n; ++i) {
    ll tmp;
    cin >> tmp;
    cubes.push_back(tmp);
  }

  for (int i = 0; i < n / 2; ++i) {
    if (i % 2 == 0) {
      ll tmp = cubes[n - i - 1];
      cubes[n - i - 1] = cubes[i];
      cubes[i] = tmp;
    }
  }

  for (int i = 0; i < n; ++i) {
    cout << cubes[i];
    if (i != n - 1) {
      cout << " ";
    }
  }
  cout << "\n";
  
  return 0;
}
