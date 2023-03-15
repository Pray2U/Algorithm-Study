def solution(s):
    answer = 1
    fir = s[0]
    fir_cou = 1
    dif_cou = 0
    for char in s[1:]:
        if fir_cou == dif_cou:
            answer += 1
            fir = char
            fir_cou = 1
            dif_cou = 0
            continue
        if char == fir:
            fir_cou += 1
        else:
            dif_cou += 1

    return answer