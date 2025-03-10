from collections import defaultdict
import sys

sys.setrecursionlimit(10 ** 6)

N = 12
WASD = [[0, 1], [0, -1], [1, 0], [-1, 0]]


# just copied ruby code
def move(log: list):
    # 到達すると 1が返るので、それが加算されていく
    if len(log) == N + 1:
        return 1
    cnt = 0
    for mv in WASD:
        next_pos = [log[-1][0] + mv[0], log[-1][1] + mv[1]]
        # next_pos が存在しないのであれば、再帰的に呼び出す
        if next_pos not in log:
            cnt += move(log + [next_pos])
    return cnt


def main():
    return move([[0, 0]])
