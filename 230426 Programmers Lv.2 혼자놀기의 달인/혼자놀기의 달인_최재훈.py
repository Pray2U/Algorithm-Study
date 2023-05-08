def solution(cards):
    answer_list, visitied_list = [], [0] * (len(cards))
    
    for target in cards:
        if not visitied_list[target-1]:
            tmp = []
            while target not in tmp:
                tmp.append(target)
                target = cards[target-1]
                visitied_list[target-1] = 1
            answer_list.append(len(tmp))
    
    if answer_list[0] == len(cards):
        return 0
    else:
        answer_list.sort(reverse=True)
        ans = answer_list[0] * answer_list[1]
    return ans

print(solution([8,6,3,7,2,5,1,4])) #12