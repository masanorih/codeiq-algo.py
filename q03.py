# フラグの状態を文字列にして返す
def flags2img(l: list):
    s = ""
    for i in range(100):
        v = l[i]
        if v == 1:
            s += f"{i+1:02} "
        else:
            s += " - "
    return s


def main():
    flags = [0] * 100
    for i in range(2, 101):
        for j in range(i, 101, i):
            idx = j - 1
            if flags[idx] == 0:
                flags[idx] = 1
            else:
                flags[idx] = 0
    r = []
    for i in range(100):
        if flags[i] == 0:
            r.append(i+1)
    return r
