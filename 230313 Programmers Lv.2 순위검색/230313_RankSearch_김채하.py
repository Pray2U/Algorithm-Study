from itertools import product
import bisect


def solution(info, query):
    items = [['cpp', "java", "python"], ["backend", "frontend"], ["junior", "senior"], ["chicken", "pizza"]]
    val = list(product(*items))
    val_dic = {''.join(v[:4]): [] for v in val}

    answer = []

    for inf in info:
        value = inf.split(" ")
        key = ''.join(value[:4])
        score = int(value[4])
        val_dic[key] += [score]

    for cnt in val_dic.keys():
        val_dic[cnt] = sorted(val_dic[cnt])

    for con in query:
        corect = 0
        con = con.replace(" and ", " ")
        li = con.split()
        conli = []

        for ind, condition in enumerate(li):
            if ind == 4:
                if condition == '-':
                    conli.append([0])
                else:
                    conli.append([int(condition)])
            elif condition == '-':
                conli.append(items[ind])
            else:
                conli.append([condition])

        for condi in list(product(*conli)):
            score = condi[4]
            condi = ''.join(condi[:4])
            corect += len(val_dic[condi]) - bisect.bisect_left(val_dic[condi], score)
        answer += [corect]
    return answer