if __name__ == '__main__':
    k, a, b = input().split()
    k, a, b, = int(k), int(a), int(b)

    count = 0

    if a >= k:
        count += int(a / k)
    if b >= k:
        count += int(b / k)

    if count == 0:
        print(-1)
    else:
        print(count)
