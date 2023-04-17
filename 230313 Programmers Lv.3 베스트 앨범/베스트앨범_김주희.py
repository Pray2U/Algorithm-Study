def solution(genres, plays):
    dic = {}
    answer = []
    for i in range(len(genres)):
        if genres[i] not in dic:
            dic[genres[i]] = [[plays[i], i]]
        else:
            dic[genres[i]].append([plays[i], i])
    score = {}
    for key in dic.keys():
        a = dic[key]
        scores = 0
        for b in a:
            scores += b[0]
        score[key] = scores

    score = sorted(score.items(), key=lambda x: x[1], reverse=True)

    for j in score:
        rank = sorted(dic[j[0]], key=lambda x: (x[0], -x[1]), reverse=True)
        if len(rank) == 1:  # 곡이 하나일 경우
            answer.append(rank[0][1])
        else:
            for i in range(2):
                answer.append(rank[i][1])
    return answer