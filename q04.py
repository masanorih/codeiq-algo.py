def cutbar(N, M, cur: int):
    if cur >= N:
        return 0
    elif cur < M:
        return 1 + cutbar(N, M, cur * 2)
    else:
        return 1 + cutbar(N, M, cur + M)


def main(N, M: int):
    cnt = 0
    chunks = [N]
    for _ in range(100):
        # while(True):
        new = []
        count_1cm = 0
        times_of_cut = min(len(chunks), M)
        times = 0
        for c in chunks:
            # 既に 1cmの棒は切り分けない
            if c != 1:
                q, mod = divmod(c, 2)
                new.append(q)
                if mod == 0:
                    new.append(q)
                else:
                    new.append(q+1)
                # 切り分け回数上限に達したらそれ以上切り分けない
                times += 1
                # print(f"{new=}, {times=}")
                if times == times_of_cut:
                    rest = chunks[times+count_1cm:]
                    # 1cmの棒を考慮する必要がある
                    # print(f"{rest=}")
                    new.extend(rest)
                    break
            else:
                count_1cm +=1
        cnt += 1
        chunks = new
        print(f"{cnt=}, {chunks=}, {times_of_cut=}, {times=}")
        if len(chunks) == chunks.count(1):
            # print(f"all chunks are 1. {chunks=}")
            break
    return cnt
