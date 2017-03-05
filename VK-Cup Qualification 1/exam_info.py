""" Created by Shahen Kosyan on 3/4/17 """

if __name__ == "__main__":
    n = int(input())
    arr = [int(x) for x in input().split()]

    users = []
    invited_users = []
    messages_count = 0
    output = ''
    for i in range(len(arr)):
        users.append([i, arr[i]])

    sender = users[0]
    users = users[1:]
    users.sort(key=lambda row: row[1])

    while messages_count != n - 1 and len(users) > 0:
        invites_count = sender[1]
        person = sender[0]
        if invites_count == 0:
            break
        while invites_count != 0:
            invited_user = users[len(users) - 1]
            invited_users.append(invited_user)
            users = users[:-1]
            output += str(person + 1) + ' ' + str(invited_user[0] + 1) + '\n'
            invites_count -= 1
            messages_count += 1
            if messages_count == n - 1:
                break

        if len(invited_users) > 0:
            sender = invited_users[0]
            invited_users = invited_users[1:]

    if messages_count < n - 1:
        print(-1)
    else:
        print(messages_count)
        print(output)
