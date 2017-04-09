""" Created by Shahen Kosyan on 4/5/17 """

if __name__ == "__main__":
    vowels = ['a', 'e', 'i', 'o', 'u', 'y']

    n = int(input())
    word = input()

    answer = ""
    i = 0
    s_count = 1
    while i < n:
        symbol = word[i]
        if i == n - 1:
            if s_count == 2 and (symbol == "e" or symbol == "o"):
                answer += symbol + symbol
                s_count = 1
            else:
                answer += symbol
        else:
            if symbol == word[i + 1] and symbol in vowels:
                s_count += 1
            elif s_count == 2 and (symbol == "e" or symbol == "o"):
                answer += symbol + symbol
                s_count = 1
            elif s_count > 1 and symbol in vowels:
                s_count = 1
                answer += symbol
            else:
                s_count = 1
                answer += symbol

        i += 1

    print(answer)
