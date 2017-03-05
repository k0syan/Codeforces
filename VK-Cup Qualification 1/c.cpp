#include <iostream>
using namespace std;

int main() {
  int n, m, k;
  cin >> n >> m >> k;
  
  char l[n][m];
  int ci, cj;
  
  for (int i = 0; i < n; ++i) {
    for (int j = 0; j < m; ++j) {
      char symbol;
      cin >> symbol;
      if (symbol == 'X') {
        ci = i;
        cj = j;
        l[i][j] = '.';
      } else {
        l[i][j] = symbol;
      }
    }
  }
  
  if (k % 2 != 0) {
    cout << "IMPOSSIBLE" << endl;
    return 0;
  }
  
  int steps = 0;
  string answer = "";
  
  while (steps < k / 2) {
    if (ci < n && l[ci + 1][cj] == '.') {
      // down
      answer += "D";
      ++ci;
    } else if (cj > 0 && l[ci][cj - 1] == '.') {
      // left
      answer += "L";
      --cj;
    } else if (cj < m && l[ci][cj + 1] == '.') {
      // right
      answer += "R";
      ++cj;
    } else if (ci > 0 && l[ci - 1][cj] == '.') {
      // up
      answer += "U";
      --ci;
    } else {
      cout << "IMPOSSIBLE" << endl;
      return 0;
    }
    
    ++steps;
  }
  
  for (int i = answer.length() - 1; i >= 0; --i) {
    switch (answer[i]) {
      case 'U': {
        answer += "D";
        break;
      }
      case 'R': {
        answer += "L";
        break;
      }
      case 'D': {
        answer += "U";
        break;
      }
      case 'L': {
        answer += "R";
        break;
      }
    }
  }
  
  cout << answer << endl;
  return 0;
}
