from itertools import product


queue = [0] * 20 + [1] * 10
# queue = [
#     0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
#     0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
#     1, 1, 1, 1, 1, 1, 1, 1, 1, 1
# ]

def main():
    cnt = 0
    for v in product(queue, repeat=len(queue)):
        found_same = False
        for i in range(len(queue)):
            l = queue[0:i+1]
            r = queue[i+1:]
            # 左右の 0 と 1 の数が同じかどうか
            l0 = l.count(0)
            r0 = r.count(0)
            if l0 == r0:
                l1 = l.count(1)
                r1 = r.count(1)
                if l1 == r1:
                    found_same = True
                    break
        if not found_same:
            cnt += 1
    return cnt
