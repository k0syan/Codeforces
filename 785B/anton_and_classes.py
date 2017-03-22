""" Created by Shahen Kosyan on 3/15/17 """

if __name__ == "__main__":
    n = int(input())

    earliest_finish_chess = 2000000000
    latest_start_chess = 0
    earliest_finish_prog = 2000000000
    latest_start_prog = 0
    i = 0
    while i < n:
        time = [int(x) for x in input().split()]
        if earliest_finish_chess > time[1]:
            earliest_finish_chess = time[1]

        if latest_start_chess < time[0]:
            latest_start_chess = time[0]
        i += 1

    m = int(input())
    i = 0
    while i < m:
        time = [int(x) for x in input().split()]
        if latest_start_prog < time[0]:
            latest_start_prog = time[0]

        if earliest_finish_prog > time[1]:
            earliest_finish_prog = time[1]
        i += 1

    if latest_start_prog - earliest_finish_chess <= 0:
        if latest_start_chess - earliest_finish_prog > 0:
            print(latest_start_chess - earliest_finish_prog)
        else:
            print(0)
    else:
        if latest_start_prog - earliest_finish_chess > latest_start_chess - earliest_finish_prog:
            print(latest_start_prog - earliest_finish_chess)
        else:
            print(latest_start_chess - earliest_finish_prog)
