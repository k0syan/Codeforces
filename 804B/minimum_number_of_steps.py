""" Created by Shahen Kosyan on 5/4/17 """

if __name__ == "__main__":
    s = input()
    total = 0

    i = 0

    if len(s) == 1:
        print(0)
        exit()

    while i < len(s) - 1:
        if i == len(s) - 2:
            if s[i] == 'a' and s[i + 1] == 'b':
                s = s[0:i] + 'bba'
                total += 1
            break
        if s[i] == 'a' and s[i + 1] == 'b':
            s = s[0:i] + 'bba' + s[i + 2:len(s)]
            total += 1
            i += 1

        if s[i] == 'a' and s[i + 1] == 'a' and s[i + 2] == 'b':
            s = s[0:i] + 'bbbbaa' + s[i + 3: len(s)]
            total += 3
            i += 3

        if s[i] == 'b' and s[i + 1] == 'a' and s[i + 2] == 'b':
            s = s[0:i] + 'bbba' + s[i + 3: len(s)]
            total += 1
            i += 2

        print(s)
        i += 1

    print(total % 1000000007)
