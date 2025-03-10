from itertools import combinations_with_replacement

OP = ["+", "-", "*", "/", ""]

def main():
    oplist = list(combinations_with_replacement(OP, 3))
    for i in range(len(oplist)):
        op = oplist[i]
        # 全ての演算子が "" は許容しない
        if op[0] == "" and op[1] == "" and op[2] == "":
            oplist.pop(i)
            break

    r = []
    for i in range(1000, 10000, 1):
        s = str(i)
        # 0 を含む数字は含めないらしい
        zero_count = s.count("0")
        if zero_count != 0:
            continue
        # rs = 逆順にした文字列。文字列の反転は reversed より s[::-1] の方が楽
        rs = int(s[::-1])
        for op in oplist:
            expression = s[0] + op[0] + s[1] + op[1] + s[2] + op[2] + s[3]
            ev = int(eval(expression))
            if rs == ev:
                r.append(i)
    # 重複を削除
    return list(set(r))
