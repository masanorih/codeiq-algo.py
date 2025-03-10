EU = [0,32,15,19,4,21,2,25,17,34,6,27,13,36,11,30,8,23,10,5,24,16,33,1,20,14,31,9,22,18,29,7,28,12,35,3,26]
US = [0,28,9,26,30,11,7,20,32,17,5,22,34,15,3,24,36,13,1,00,27,10,25,29,12,8,19,31,18,6,21,33,16,4,23,35,14,2]

def get_sum(idx, i: int, tables: list):
    """get_sum
    ルーレットの数字を前後を含めた合計を返す
    Args:
        idx: 数字
            示されている値
        i: 数字
            連続する個数
        tables: リスト
            ヨーロッパスタイルかアメリカンスタイルか
    Returns: 数字
    """
    a = tables[idx -1]
    b = tables[idx]
    if idx == 35:
        c = tables[0]
    else:
        c = tables[idx +1]
    return a + b + c


# tables の各 0..maxvalの合計値のリストを生成して返す
def get_maxsum(maxval: int, tables: list):
    tlen = len(tables)
    tables.extend(tables)
    sumlist = list()
    for n in range(0, tlen, 1):
        nlist = tables[n:maxval+n]
        sumlist.append(nlist)
    return sumlist


# 2つのリストの最大値を返す
def get_maxvals(eu, us: list):
    eu_max, us_max = 0, 0
    # eu, us 共に配列の長さは同じなので同じループで
    for i in range(len(eu)):
        eu_sum = sum(eu[i])
        if eu_max < eu_sum:
            eu_max = eu_sum
        us_sum = sum(us[i])
        if us_max < us_sum:
            us_max = us_sum
    return eu_max, us_max


# 36個のリストをまず生成し、おしりを 1個ずつ減らしながら最大値を比較していく
def main():
    cnt = 0
    eu_maxlist = get_maxsum(36, EU)
    us_maxlist = get_maxsum(36, US)
    # 36 の max を取得して比較
    eu_max, us_max = get_maxvals(eu_maxlist, us_maxlist)
    if eu_max < us_max:
        cnt += 1

    # 35..2 の max も取得して比較する
    for x in range(35, 1, -1):
        for i in range(len(eu_maxlist)):
            eu_maxlist[i].pop(-1)
        for i in range(len(us_maxlist)):
            us_maxlist[i].pop(-1)
        eu_max, us_max = get_maxvals(eu_maxlist, us_maxlist)
        if eu_max < us_max:
            cnt += 1
    return cnt
