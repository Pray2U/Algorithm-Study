# Solution 02

def solution(genres, plays):
    answer = []
    each_play, total_play = {}, {}

    for idx, (genre, play) in enumerate(zip(genres, plays)):
        if genre not in each_play:
            each_play[genre] = [(idx, play)]
        else:
            each_play[genre].append((idx, play))

        if genre not in total_play:
            total_play[genre] = play
        else:
            total_play[genre] += play

    for (genre_key, _) in sorted(total_play.items(), key=lambda x:x[1], reverse=True):
        for (target_idx, _) in sorted(each_play[genre_key], key=lambda x:x[1], reverse=True)[:2]:
            answer.append(target_idx)
    print(f"total_play ; {total_play}")
    print(f"each_play ; {each_play}")
    return answer


print(solution(["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500])) # [4, 1, 3, 0]