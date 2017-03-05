""" Created by Shahen Kosyan on 3/4/17 """

if __name__ == "__main__":
    n = int(input())
    arr = [int(x) for x in input().split()]

    arr = sorted(arr)

    print(arr[len(arr) // 2])
