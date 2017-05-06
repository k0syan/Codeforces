""" Created by Shahen Kosyan on 5/4/17 """

if __name__ == "__main__":
    l, r = [int(x) for x in input().split()]

    if r - l > 0:
        print(2)
    else:
        print(r)
