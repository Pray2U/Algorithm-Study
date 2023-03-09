def solution(s):
    answer = 0

    if s.count('(') != s.count(')') or s.count('[') != s.count(']') or s.count('{') != s.count('}'):
        return 0

    for i in range(len(s)):
        ch_s = s
        for j in range(len(s) // 2):
            ex_s = ch_s
            ch_s = ch_s.replace("()", "")
            ch_s = ch_s.replace("[]", "")
            ch_s = ch_s.replace("{}", "")
            if ch_s == ex_s:
                break
            elif ch_s == '':
                answer += 1
                break
        s = s[1:] + s[0]
    return answer