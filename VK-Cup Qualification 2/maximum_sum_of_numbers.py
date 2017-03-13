""" Created by Shahen Kosyan on 3/11/17 """

if __name__ == "__main__":
    x = input()

    if int(x) < 10:
        print(x)
        exit()

    arr = [int(a) for a in list(x)]
    x_sum = sum(arr)

    i = len(arr) - 1
    answer = ''
    while i > 0:
        if arr[i] != 9 and arr[i] != 8:
            arr[i - 1] -= 1
            answer = '9' + answer
        else:
            change = False
            for j in range(i - 1, 0, -1):
                if arr[j] < 9:
                    change = True
                    break

            if arr[i] == 8 and change:
                answer = '9' + answer
                arr[i - 1] -= 1
            else:
                if not change:
                    answer = str(arr[i]) + answer
                else:
                    answer = '9' + answer

        if i == 1 and arr[0] != 0:
            answer = str(arr[0]) + answer
        i -= 1

    answer = [int(a) for a in list(answer)]
    if x_sum == sum(answer):
        print(x)
    else:
        answer = [str(a) for a in answer]
        print(''.join(answer))
