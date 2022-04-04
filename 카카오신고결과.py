

def solution(id_list, report, k):
    answer = [0] * len(id_list)
    singo_dict = {id: [] for id in id_list}

    for r in set(report):
        from_r, to_r = r.split(' ')
        singo_dict[to_r].append(from_r)

    for key, value in singo_dict.items():
        if len(value) >= k:
            for v in value:
                answer[id_list.index(v)] += 1
    return answer