""" Created by Shahen Kosyan on 4/21/17 """

if __name__ == "__main__":
    s = input()
    count = 0
    possible = True
    for i in range(int(len(s) / 2)):
        if s[i] != s[len(s) - i - 1]:
            count += 1
            if count > 1:
                possible = False
                break

    if len(s) % 2 == 1 and count == 0:
        count += 1

    if possible and count == 1:
        print('YES')
    else:
        print('NO')
