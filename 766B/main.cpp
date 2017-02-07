#include <iostream>
using namespace std;
typedef unsigned long long huge;

huge getMax(huge arr[], int n) {
  huge max = arr[0];

  for (int i = 1; i < n; i++)
    if (arr[i] > max)
      max = arr[i];

  return max;
}

void countSort(huge arr[], int n, int exp) {
  huge output[n];
  int i, count[10] = {0};

  for (i = 0; i < n; i++)
    count[(arr[i] / exp) % 10]++;

  for (i = 1; i < 10; i++)
    count[i] += count[i - 1];

  for (i = n - 1; i >= 0; i--) {
    output[count[(arr[i] / exp) % 10] - 1] = arr[i];
    count[(arr[i] / exp) % 10]--;
  }

  for (i = 0; i < n; i++)
    arr[i] = output[i];
}

void radixsort(huge arr[], int n) {
  huge m = getMax(arr, n);
  for (int exp = 1; m / exp > 0; exp *= 10)
    countSort(arr, n, exp);
}


int main() {

  int count;
  bool possibility = false;

  cin >> count;
  huge lengths[count];
  for (int i = 0; i < count; ++i) {
    cin >> lengths[i];
  }

  radixsort(lengths, count);

  for (int i = 0; i < count - 2; ++i) {
    if (lengths[i] + lengths[i + 1] > lengths[i + 2]) {
      possibility = true;
      break;
    }
  }

  if (possibility) {
    cout << "YES" << endl;
  } else {
    cout << "NO" << endl;
  }

  return 0;
}