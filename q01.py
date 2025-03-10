def is_kaibun(s: str):
    """is_kaibun
    文字列 sが回文かどうかを判定する
    戻り値
        True:  sは回文である
        False: sは回文ではない
    """
    # 再帰的動作中に文字列長が 1以下になれば、それは回文である
    if len(s) <= 1:
        return True
    sl = list(s)
    first = sl.pop(0)
    last = sl.pop(-1)
    if first == last:
        return is_kaibun(sl)
    return False


def main():
    # 11 からの奇数だけを探せばよいから、+2づつする
    for i in range(11, 10000, 2):
        # D: 10進数, B: 2進数, O: 8進数
        D, B, O = str(i), bin(i), oct(i)
        if is_kaibun(D) and is_kaibun(B[2:]) and is_kaibun(O[2:]):
            return i
