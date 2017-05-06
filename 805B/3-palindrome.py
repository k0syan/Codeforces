""" Created by Shahen Kosyan on 5/4/17 """

if __name__ == "__main__":
    n = int(input())
    answer = 'b'

    for i in range(n - 1):
        if answer[i] == 'b' and (i + 1) % 2 == 1:
            answer += 'b'

        if answer[i] == 'b' and (i + 1) % 2 == 0:
            answer += 'a'

        if answer[i] == 'a' and (i + 1) % 2 == 1:
            answer += 'a'

        if answer[i] == 'a' and (i + 1) % 2 == 0:
            answer += 'b'

    print(answer)
