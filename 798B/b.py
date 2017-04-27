""" Created by Shahen Kosyan on 4/21/17 """

if __name__ == "__main__":
    n = int(input())
    strings = []

    for i in range(n):
        strings.append(input())

    minimum = 50000

    for i in range(n):
        count = 0
        for j in range(n):
            s = strings[j][:]
            if j == i:
                continue
            steps = 0
            while s != strings[i]:
                char = s[0]
                s = s[1:]
                s += char
                count += 1
                steps += 1
                if steps > len(s):
                    print('-1')
                    exit()
        if count < minimum:
            minimum = count

    print(minimum)
