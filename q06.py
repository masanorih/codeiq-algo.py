# 1になるまで操作を繰り返して数字を変化させ、最初の数に戻るかチェックする
def is_loop(N: int):
    check = N * 3 + 1
    while check != 1:
        if check % 2 == 0:
            check /= 2
        else:
            check = check * 3 + 1
        if check == N:
            return True
    return False


def main():
    cnt = 0
    for N in range(2, 10000, 2):
        if is_loop(N):
            cnt += 1
    return cnt
