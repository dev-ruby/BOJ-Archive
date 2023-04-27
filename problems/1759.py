# 1759 - 암호 만들기

import sys


def solve():
    input = sys.stdin.readline

    l, c = map(int, input().split())
    letters = sorted(input().split())
    stack = []

    def count_vowel(word):
        count = 0
        vowels = "aeiou"
        for w in word:
            if w in vowels:
                count += 1

        return count

    def count_consonant(word):
        vowel_count = count_vowel(word)
        count = len(word) - vowel_count

        return count

    def find_password(depth=0):
        nonlocal stack
        if depth == l:
            word = "".join(stack)
            if (count_vowel(word) >= 1) and (count_consonant(word) >= 2):
                print(word)
            return

        for w in letters:
            if stack:
                if w in stack:
                    continue
                if ord(stack[-1]) > ord(w):
                    continue

            stack.append(w)
            find_password(depth + 1)
            stack.pop()

    find_password()


if __name__ == "__main__":
    solve()
