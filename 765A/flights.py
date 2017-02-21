""" Created by Shahen Kosyan """

if __name__ == '__main__':
    n = int(input())
    home_airport = input()
    flights = []
    while n > 0:
        n -= 1
        _from, _to = input().split('->')
        flights.append(_from)
        flights.append(_to)

    count = 0

    for i in range(len(flights)):
        if flights[i] == home_airport:
            count += 1

    if count % 2:
        print('contest')
    else:
        print('home')
