# 1924 - 2007년

import sys
import datetime


def solve():
    input = sys.stdin.readline

    m, d = map(int, input().split())
    today = datetime.datetime(2007, m, d)
    print(["MON", "TUE", "WED", "THU", "FRI", "SAT", "SUN"][today.weekday()])


if __name__ == "__main__":
    solve()
