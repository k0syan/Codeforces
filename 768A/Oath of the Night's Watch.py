""" Created by Shahen Kosyan """

if __name__ == '__main__':
    n = int(input())
    strenghts = [int(s) for s in input().split()]

    minimum = min(strenghts)
    maximum = max(strenghts)

    count = 0

    for i in range(n):
        if minimum < strenghts[i] < maximum:
            count += 1

    print(count)
