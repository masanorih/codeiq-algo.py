from datetime import datetime, timedelta


# ymd: YYYYMMDD の文字列
def calc_ymd(ymd: str):
    b = bin(int(ymd))
    bo = b[2:]          # bit only: 先頭の '0b' を除いた文字列
    rb = bo[::-1]       # reversed bit: bit だけの文字列の反転
    rd = int(rb, 2)     # reversed decimal: 反転したbit文字列を10進数の整数化
    return str(rd)


def main():
    r = []
    ymd = ""
    d = datetime.strptime("19641010", "%Y%m%d")
    while ymd != "20200724":
        ymd = d.strftime("%Y%m%d")
        if ymd == calc_ymd(ymd):
            r.append(ymd)
        d += timedelta(days=1)
    return r
