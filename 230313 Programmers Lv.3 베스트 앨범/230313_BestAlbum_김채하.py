def solution(genres, plays):
    answer = []
    sum_dic = {x : 0 for x in set(genres)}
    dic = {x : [] for x in set(genres)}
    for ind, gen in enumerate(genres):
        dic[gen] += [(plays[ind],ind)]
        sum_dic[gen] += plays[ind]
    sum_dic = sorted(sum_dic.items(), key = lambda x : x[1], reverse=True)
    for ge in sum_dic:
        song = ge[0]
        dic[song].sort(key = lambda x : (-x[0],x[1]))
        answer += [dic[song][0][1]]
        if len(dic[song]) >= 2:
            answer += [dic[song][1][1]]
    return answer