""" Created by Shahen Kosyan on 3/11/17 """

if __name__ == "__main__":
    n, k = [int(x) for x in input().split()]
    kc = k

    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    alphabet = list(alphabet)
    password = ''

    i = 0
    while kc > 0:
        password += alphabet[i]
        kc -= 1
        i += 1

    i = 0
    while len(password) < n:
        if i == k:
            i = 0
        password += password[i]
        i += 1

    print(password)
