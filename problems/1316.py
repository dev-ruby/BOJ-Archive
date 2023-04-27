# 1316 - 그룹 단어 체커

import sys


def solve():
    input = sys.stdin.readline

    n = int(input())
    count = 0
    for i in range(n):
        alphabet = list("abcdefghijklmnopqrstuvwxyz")
        word = input()
        c = 1
        for w in range(len(word)):
            if w == 0:
                alphabet.remove(word[w])
                continue
            else:
                if word[w] in alphabet:
                    alphabet.remove(word[w])
                    continue
                else:
                    if word[w - 1] == word[w]:
                        continue
                    else:
                        c = 0
        count += c
    print(count)


if __name__ == "__main__":
    solve()
