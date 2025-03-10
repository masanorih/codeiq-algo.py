"""
2-15枚の硬貨の組み合わせを全て列挙して、合計額が1000円になる組み合わせを数える
"""
from itertools import combinations_with_replacement


def main():
    coins = [10, 50, 100, 500]
    cnt = 0
    for i in range(2, 16):
        for v in combinations_with_replacement(coins, i):
            if 1000 == sum(v):
                cnt += 1
    return cnt
