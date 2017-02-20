if __name__ == '__main__':
    n = int(input())
    strenghts = input().split()
    strenghts = [int(s) for s in strenghts]

    maximum = max(strenghts)
    minimum = min(strenghts)

    count = 0

    for i in range(n):
        if minimum < strenghts[i] < maximum:
            count += 1

    print(count)
