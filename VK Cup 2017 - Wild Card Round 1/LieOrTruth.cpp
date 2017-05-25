#include <iostream>
#include <vector>
#include <algorithm>
#include <iterator>
using namespace std;

typedef long long ll;

int main() {
  int n, l, r;
  
  cin >> n >> l >> r;
  vector<int> vasya;
  vector<int> stepan;
  
  for (int i = 0; i < n; ++i) {
    int tmp;
    cin >> tmp;
    vasya.push_back(tmp);
  }
  
  for (int i = 0; i < n; ++i) {
    int tmp;
    cin >> tmp;
    stepan.push_back(tmp);
  }
  
  vector<int> vasya_1;
  vector<int> stepan_1;
  
  for (int i = l - 1; i < r; ++i) {
    vasya_1.push_back(vasya[i]);
    stepan_1.push_back(stepan[i]);
  }
  
  sort(begin(vasya_1), end(vasya_1));
  sort(begin(stepan_1), end(stepan_1));
  
  bool truth = true;

  for (int i = 0; i < vasya_1.size(); ++i) {
    if (vasya_1[i] != stepan_1[i]) {
      truth = false;
      break;
    }
  }  
  
  if (truth) {
    for (int i = 0; i < l - 1; ++i) {
      if (vasya[i] != stepan[i]) {
        truth = false;
        break;
      }
    }
    for (int i = r; i < n; ++i) {
      if (vasya[i] != stepan[i]) {
        truth = false;
        break;
      }
    }
  }
    
  if (truth) {
    cout << "TRUTH" << '\n';
  } else {
    cout << "LIE" << '\n';
  }
  
  return 0;
}
