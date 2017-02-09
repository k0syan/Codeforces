#include <iostream>
#include <vector>
typedef long long big;
using namespace std;

int main() {
  int n;
  cin >> n;
  vector<big> cubes;
  for (int i = 0; i < n; ++i) {
    big tmp;
    cin >> tmp;
    cubes.push_back(tmp);
  }

  for (int i = 0; i < n / 2; ++i) {
    if (i % 2 == 0) {
      big tmp = cubes[n - i - 1];
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
  
  cout << endl;

  return 0;
}
