""" Created by Shahen Kosyan """

if __name__ == '__main__':
    k, a, b = [int(x) for x in input().split()]

    count = 0

    if a >= k:
        count += a // k
    if b >= k:
        count += b // k

    if count == 0:
        print(-1)
    else:
        print(count)
