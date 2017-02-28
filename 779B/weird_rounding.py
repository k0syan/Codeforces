""" Created by Shahen Kosyan on 2/26/17 """

if __name__ == "__main__":
    n, k = [int(x) for x in input().split()]
    digits = list(str(n))

    zero_count = digits.count('0')
    count = 0
    if zero_count < k:
        count = len(str(n)) - 1

    x = n
    for i in range(len(str(x))):
        if x % 10 != 0:
            count += 1
        else:
            zero_count += 1

        x //= 10

        if zero_count == k:
            break

    print(count)
